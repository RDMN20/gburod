from abc import ABC, abstractmethod
from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from personnels.models import (
    Department,
    Persona,
)


class BaseSitemap(Sitemap, ABC):
    changefreq = "weekly"
    priority = 0.5

    @abstractmethod
    def items(self):
        pass

    def lastmod(self, obj):
        pass


class DepartmentSitemap(BaseSitemap):
    def items(self):
        return Department.objects.all()


class PersonaSitemap(BaseSitemap):
    def items(self):
        return Persona.objects.all()

    def lastmod(self, obj):
        return obj.updated_at


class StaticSitemap(Sitemap):
    """Reverse 'static' views for XML sitemap."""
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        # Return list of url names for views to include in sitemap
        return [
            'main-page:index',
            'main-page:diag-research',
            'main-page:about',
            'main-page:patients',
            'main-page:privacy'
            'structure:licenses',
            'structure:structures',
            'paid-services:services',
        ]

    def location(self, item):
        return reverse(item)
