from django.conf import settings
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from .models import News


def get_page_obj(posts, page_number):
    """Paginator"""
    paginator = Paginator(posts, settings.AMOUNT_NEWS_ONE_PAGE)
    return paginator.get_page(page_number)


def news_list(request):
    """Представление для отображения всех новостей"""
    template = 'news/news_list.html'
    news = News.objects.filter(is_published=True)

    if news:
        page_obj = get_page_obj(news, request.GET.get('page'))
    else:
        page_obj = None

    context = {
        'page_obj': page_obj,
    }

    return render(request, template, context)


def news_detail(request, news_id):
    """Представление для детального отображения новостей"""
    news = get_object_or_404(News, id=news_id)

    context = {
        'news': news,
    }

    return render(request, 'news/news_detail.html', context)
