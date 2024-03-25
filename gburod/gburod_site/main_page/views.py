from django.shortcuts import render

from news_posts.models import News


def index(request):
    template = 'main_page/index.html'
    latest_news = News.objects.filter(
        is_published=True
    ).order_by('-pub_date')[:3]
    default_image_path = 'img/default_image.jpg'
    context = {
        'latest_news': latest_news,
        'default_image_path': default_image_path,
    }

    return render(request, template, context)


def about_us(request):
    template = 'main_page/about.html'
    return render(request, template)


def privacy(request):
    template = 'main_page/privacy.html'
    return render(request, template)


def for_patients(request):
    template = 'main_page/for_patients.html'
    return render(request, template)


def diag_research(request):
    template = 'main_page/prep_diag_research.html'
    return render(request, template)
