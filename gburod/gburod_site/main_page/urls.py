from django.urls import path

from .views import (
    index, about_us, privacy,
    for_patients, diag_research,
)


app_name = 'main-page'
urlpatterns = [
    path('', index, name='index'),
    path('about/', about_us, name='about'),
    path('privacy/', privacy, name='privacy'),
    path('patients/', for_patients, name='patients'),
    path('diag-research/', diag_research, name='diag-research'),
]
