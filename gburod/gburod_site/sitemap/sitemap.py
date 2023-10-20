from django.contrib import sitemaps
from django.urls import reverse
from django.urls import get_resolver


class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        resolver = get_resolver(None)
        url_names = []

        for url_pattern in resolver.url_patterns:
            if url_pattern.name:
                url_names.append(url_pattern.name)

        return url_names

    def location(self, item):
        return reverse(item)
