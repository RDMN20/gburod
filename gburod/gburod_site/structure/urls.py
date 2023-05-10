from django.urls import path

from . import views

app_name = 'structure'
urlpatterns = [
    path('', views.structures, name='structures'),
    path('ambulant/', views.ambulant, name='ambulant'),
    path('depart_detail/<int:department_id>/', views.depart_detail, name='depart_detail'),
    path('persona_detail/<int:persona_id>/', views.persona_detail, name='persona_detail'),
    path(
        'persona_detail/qr/<int:persona_code>/',
        views.persona_qr_detail,
        name='persona_qr_detail',
    ),
    path('persona_detail/<int:persona_id>/comment/', views.add_comment, name='add_comment'),
    path('licenses/', views.licenses, name='licenses'),
    # path('licenses/<int:pk>/preview/', LicensePDFView.as_view(), name='license_preview'),
    # path('licenses/<int:license_id>/preview/', views.license_preview, name='license_preview'),
    # path('licenses/<int:pk>/', views.license_preview, name='license_preview'),
]
