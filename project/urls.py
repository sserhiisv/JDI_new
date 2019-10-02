from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.conf.urls.i18n import i18n_patterns

from apps.webapp.sitemap import *


sitemaps = {
    'posts': PostSitemap,
    'events': EventSitemap,
    'facts': FactSitemap,
}

urlpatterns = [
    url(r'^i18n/', include('django.conf.urls.i18n')),
]

urlpatterns += i18n_patterns(
    url(r'^admin/', include(admin.site.urls)),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    url(r'^hitcount/', include('hitcount.urls', namespace='hitcount')),
    url(r'^', include('webapp.urls')),
)
