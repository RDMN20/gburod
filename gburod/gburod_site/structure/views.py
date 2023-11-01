import datetime
from django.utils import timezone
from django.conf import settings
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.core.paginator import Paginator
from django.db.models import Avg, Count
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from decimal import Decimal

from personnels.forms import RatingForm, CommentForm
from personnels.models import Persona, Department, Rating
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
    """Подробно об отделении"""
    template = 'structure/department_detail.html'
    departs = Department.objects.all()
    department = get_object_or_404(departs, id=department_id)
    current_page_id = department_id
    personas = department.persona.filter(published=True).annotate(score_count=Count('rating'))
    page_obj = get_page_obj(personas, request.GET.get('page'))

    context = {
        'current_page_id': current_page_id,
        'department': department,
        'departs': departs,
        'page_obj': page_obj,
    }
    return render(request, template, context)


def persona_detail(request, persona_id=None, persona_code=None, department_id=None):
    """Детальное представление о сотрунике."""
    # Получаем текущее время
    now = timezone.now()
    last_minute = now - datetime.timedelta(seconds=60)

    template = 'structure/persona_detail.html'
    if persona_code:
        persona = Persona.objects.get(persona_code=persona_code)
    else:
        persona = Persona.objects.get(id=persona_id)
    ratings = persona.rating.all()
    adding_rate = persona.departments.get(id=department_id).adding_rate
    average_rating = round(
        ratings.aggregate(Avg('score'))['score__avg'] or 0,
        2
    )
    persona.avg_rating = average_rating
    persona.save()
    comments = persona.comments.select_related('author')

    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid() and request.recaptcha_is_valid:
            try:
                score = Decimal(
                    form.cleaned_data['score']).quantize(Decimal('0.01'))
                if Rating.objects.filter(
                        persona=persona, created__gte=last_minute).exists():
                    messages.error(
                        request,
                        'Вы уже оценили врача в течение последней минуты'
                    )
                else:
                    Rating.objects.create(persona=persona, score=score)
                    messages.success(request, 'Рейтинг успешно сохранен')
                return redirect(
                    'structure:persona_detail',
                    persona_id=persona.id
                )
            except ValidationError as e:
                messages.error(request, e.args[0])
    else:
        form = RatingForm()
    context = {
        'ratings': ratings,
        'average_rating': average_rating,
        'persona': persona,
        'comments': comments,
        'comment_form': CommentForm(),
        'form': form,
        'department_id': department_id,
        'adding_rate': adding_rate,
        'now': now,
    }
    return render(request, template, context)


@login_required
def add_comment(request, persona_id):
    """Добавление комментария."""
    persona = get_object_or_404(Persona, id=persona_id)
    form = CommentForm(request.POST or None)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.author = request.user
        comment.persona = persona
        comment.save()
    return redirect('structure:persona_detail', persona_id=persona_id)


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
