from django.conf import settings
from django.core.paginator import Paginator
from django.db.models import Avg
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from personnels.forms import RatingForm, CommentForm
from personnels.models import Persona, Department, Rating, Comment

# from forms import CommentForm


def get_page_obj(posts, page_number):
    paginator = Paginator(posts, settings.AMOUNT_POSTS_ONE_PAGE)
    return paginator.get_page(page_number)


def structures(request):
    depart = Department.objects.all()
    stuff = Persona.objects.filter(department__slug='administration')
    template = 'structure/structures.html'
    context = {
        'depart': depart,
        'page_obj': get_page_obj(stuff, request.GET.get('page')),
    }
    return render(request, template, context)


def depart_detail(request, department_id):
    template = 'structure/structures.html'
    depart = Department.objects.all()
    departs = get_object_or_404(Department, id=department_id)
    current_page_id = department_id
    personas = Persona.objects.filter(department=departs)
    context = {
        'current_page_id': current_page_id,
        'depart': depart,
        'page_obj': get_page_obj(personas, request.GET.get('page')),
    }
    return render(request, template, context)


def persona_detail(request, persona_id):
    template = 'structure/persona_detail.html'
    persona = Persona.objects.get(id=persona_id)
    ratings = persona.rating.all()
    average_rating = ratings.aggregate(Avg('score'))['score__avg'] or 0
    comments = persona.comments.select_related('author')
    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            score = form.cleaned_data['score']
            Rating.objects.create(persona=persona, score=score)
            return redirect('structure:persona_detail', persona_id=persona_id)
    else:
        form = RatingForm()
    context = {
        'ratings': ratings,
        'average_rating': average_rating,
        'persona': persona,
        'comments': comments,
        'comment_form': CommentForm(),
        'form': form,
    }
    return render(request, template, context)

def persona_qr_detail(request, persona_code):
    template = 'structure/persona_detail.html'
    persona = Persona.objects.get(persona_code=persona_code)
    ratings = persona.rating.all()
    average_rating = ratings.aggregate(Avg('score'))['score__avg'] or 0
    comments = persona.comments.select_related('author')
    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            score = form.cleaned_data['score']
            Rating.objects.create(persona=persona, score=score)
            return redirect('structure:persona_detail', persona_id=persona.id)
    else:
        form = RatingForm()
    context = {
        'ratings': ratings,
        'average_rating': average_rating,
        'persona': persona,
        'comments': comments,
        'comment_form': CommentForm(),
        'form': form,
    }
    return render(request, template, context)

@login_required
def add_comment(request, persona_id):
    persona = get_object_or_404(Persona, id=persona_id)
    form = CommentForm(request.POST or None)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.author = request.user
        comment.persona = persona
        comment.save()
    return redirect('structure:persona_detail', persona_id=persona_id)


def ambulant(request):
    template = 'structure/ambulant.html'
    return render(request, template)


