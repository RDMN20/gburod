from django.urls import path

from . import views
from .decorators import check_recaptcha

app_name = 'structure'
urlpatterns = [
    path('', views.structures, name='structures'),
    path('ambulant/', views.ambulant, name='ambulant'),
    path('depart_detail/<int:department_id>/', views.depart_detail,
         name='depart_detail'),
    path('persona_detail/<int:persona_id>/',
         check_recaptcha(views.persona_detail), name='persona_detail'),
    path('persona_detail/qr/<int:persona_code>/',
         check_recaptcha(views.persona_detail), name='persona_qr_detail'),
    path('persona_detail/<int:persona_id>/comment/', views.add_comment,
         name='add_comment'),
    path('licenses/', views.licenses, name='licenses'),
]
