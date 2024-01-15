"""gburod_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import path, include

from structure.sitemaps import (
    DepartmentSitemap,
    PersonaSitemap, StaticSitemap,
)
from news_posts.sitemaps import NewsSitemap


sitemaps = {
    'static': StaticSitemap,
    'departments': DepartmentSitemap,
    'personas': PersonaSitemap,
    'news': NewsSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main_page.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}),
    path('structure/', include('structure.urls')),
    path('paid_services/', include('paid_services.urls')),
    path('news/', include('news_posts.urls')),
    path('auth/', include('users.urls')),
    path('auth/', include('django.contrib.auth.urls')),

]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
    urlpatterns += static(
        settings.STATIC_URL,
        document_root=settings.STATIC_ROOT
    )
