from django.urls import path
from . import views


app_name = 'news-posts'
urlpatterns = [
    path('', views.news_list, name='news'),
]
