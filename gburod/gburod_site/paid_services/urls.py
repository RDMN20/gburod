from django.urls import path

from . import views


app_name = 'paid_services'

urlpatterns = [
    path('services/', views.paid_services, name='services'),
]
