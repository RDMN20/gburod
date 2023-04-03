from django.urls import path

from . import views


app_name = 'main-page'
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about_us, name='about'),
]
