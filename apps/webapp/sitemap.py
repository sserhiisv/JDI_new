from datetime import datetime

from django.contrib.sitemaps import Sitemap

from webapp.models import Post, Fact, Event


class PostSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return Post.objects.filter(status='published') \
                           .filter(date__lte=datetime.now())

    def lastmod(self, obj):
        return obj.date


class EventSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return Event.objects.filter(status='published')

    def lastmod(self, obj):
        return obj.date


class FactSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return Fact.objects.filter(status='published')

    def lastmod(self, obj):
        return obj.date
