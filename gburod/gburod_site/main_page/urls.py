from django.urls import path
from django.contrib.sitemaps.views import sitemap

from sitemap.sitemap import StaticViewSitemap
from . import views

sitemaps = {
    'static': StaticViewSitemap,
}

app_name = 'main-page'
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about_us, name='about'),
    path('sitemap.xml/', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap')
]
