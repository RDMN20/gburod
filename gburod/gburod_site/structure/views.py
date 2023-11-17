import datetime
from django.utils import timezone
from django.conf import settings
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.core.paginator import Paginator
from django.db.models import Avg
from django.shortcuts import render, get_object_or_404, redirect
from decimal import Decimal

from personnels.forms import RatingForm, CommentForm
from personnels.models import (
    Persona,
    Department,
    Rating,
    PersonaDepartment,
)
from structure.models import License


def get_page_obj(posts, page_number):
    """Paginator"""
    paginator = Paginator(posts, settings.AMOUNT_POSTS_ONE_PAGE)
    return paginator.get_page(page_number)


def structures(request):
    """Страница структура"""
    departs = Department.objects.all()
    template = 'structure/structures.html'
    context = {
        'departs': departs,
    }
    return render(request, template, context)


def depart_detail(request, department_id):
    template = 'structure/department_detail.html'
    departs = Department.objects.all()

    # Получаем отделение по ID или возвращаем 404, если отделение не найдено
    department = get_object_or_404(Department, id=department_id)

    # Получаем связанных сотрудников для данного отделения
    personas = Persona.objects.filter(
        persona_departments__department=department,
        published=True
    ).select_related(
        'seat',
        'academic',
        'speciality',
        'office',
        'biography'
    ).prefetch_related('persona_departments__department')

    page_obj = get_page_obj(personas, request.GET.get('page'))

    context = {
        'department': department,
        'page_obj': page_obj,
        'departs': departs,
    }
    return render(request, template, context)


def persona_detail(request, persona_id=None, persona_code=None,
                   department_id=None):
    now = timezone.now()
    last_minute = now - datetime.timedelta(seconds=60)
    template = 'structure/persona_detail.html'

    # Получаем объект Persona
    persona = get_persona(persona_id, persona_code)

    # Получаем отделения сотрудника
    persona_departments = PersonaDepartment.objects.filter(persona=persona)
    # Получаем связанные рейтинги
    ratings = Rating.objects.filter(persona=persona)

    # Получаем связанные комментарии
    comments = persona.comments.all()

    # Получаем adding_rate для отделения
    department = get_department(department_id)
    adding_rate = department.adding_rate if department else None

    if request.method == 'POST':
        raiting_form = RatingForm(request.POST)
        comment_form = CommentForm(request.POST)
        if (raiting_form.is_valid()
                and comment_form.is_valid()
                and request.recaptcha_is_valid):
            try:
                score = Decimal(raiting_form.cleaned_data['score']).quantize(
                    Decimal('0.01'))
                if Rating.objects.filter(persona=persona,
                                         created__gte=last_minute).exists():
                    messages.error(
                        request,
                        'Вы уже оценили сотрудника в течение последней минуты',
                    )
                else:
                    Rating.objects.create(
                        persona=persona,
                        score=score,
                        author=comment_form.cleaned_data['author'],
                    )
                    messages.success(request, 'Рейтинг успешно сохранен')

                    # Обновляем средний рейтинг
                    persona.avg_rating = Rating.objects.filter(
                        persona=persona
                    ).aggregate(Avg('score'))['score__avg']
                    persona.save()

                    # Вызываем функцию для добавления комментария
                    add_comment(
                        request,
                        persona.id,
                        department_id,
                        author=comment_form.cleaned_data['author'],
                    )
                return redirect(
                    'structure:persona_detail',
                    persona_id=persona.id,
                    department_id=department_id,
                )
            except ValidationError as e:
                messages.error(request, e.args[0])
    else:
        raiting_form = RatingForm()
        comment_form = CommentForm()

    context = {
        'persona': persona,
        'persona_departments': persona_departments,
        'ratings': ratings,
        'comments': comments,
        'comment_form': comment_form,
        'form': raiting_form,
        'department_id': department_id,
        'adding_rate': adding_rate,
        'now': now,
    }
    return render(request, template, context)


def get_persona(persona_id, persona_code):
    if persona_code:
        return Persona.objects.select_related(
            'biography', 'seat', 'academic', 'speciality', 'office'
        ).get(persona_code=persona_code)
    else:
        return Persona.objects.select_related(
            'biography', 'seat', 'academic', 'speciality', 'office'
        ).get(id=persona_id)


def get_department(department_id):
    try:
        return Department.objects.get(id=department_id)
    except Department.DoesNotExist:
        return None


# @login_required
def add_comment(request, persona_id, department_id, author=None):
    """Добавление комментария."""
    persona = get_object_or_404(Persona, id=persona_id)
    comment_form = CommentForm(request.POST or None)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.persona = persona
        comment.author = author
        comment.save()
    return redirect(
        'structure:persona_detail',
        persona_id=persona_id,
        department_id=department_id,
    )


def licenses(request):
    """Представление документов и лицензий организации."""
    template = 'structure/licenses.html'
    departs = Department.objects.all()
    licenses_all = License.objects.all()
    context = {
        'licenses': licenses_all,
        'departs': departs,
    }
    return render(request, template, context)


def license_preview(request, pk):
    """Предпросмотр документов."""
    license_pr = get_object_or_404(License, pk=pk)
    context = {
        'license': license_pr,
    }
    return render(request, 'structure/license_preview.html', context)


def ambulant(request):
    template = 'structure/ambulant.html'
    return render(request, template)
