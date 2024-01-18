from django.shortcuts import render

from news_posts.models import News


def index(request):
    template = 'main_page/index.html'
    latest_news = News.objects.filter(
        is_published=True
    ).order_by('-pub_date')[:3]

    context = {
        'latest_news': latest_news,
    }

    return render(request, template, context)


def about_us(request):
    template = 'main_page/about.html'
    return render(request, template)
