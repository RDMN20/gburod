from django.urls import path
from django.contrib.sitemaps.views import sitemap

from . import views


app_name = 'main-page'
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about_us, name='about'),
]
