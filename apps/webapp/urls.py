from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from webapp import views

urlpatterns = [
    url(r'^$', views.HomePage.as_view(), name="home"),
    url(r'^new_posts/$', views.NewPosts.as_view(), name="latest-posts"),
    url(r'^popular/$', views.PopularPosts.as_view(), name="popular-posts"),
    url(r'^category/(?P<slug>[-\w]+)/$', views.CategoryPosts.as_view(), name='category'),
    url(r'^post/(?P<slug>[-\w]+)/$', views.ViewPost.as_view(), name='post'),
    #url(r'^search/$', views.search, name='search'),
    #url(r'^404/$', views.handler404, name='handler404'),
    #url(r'^500/$', views.handler500, name='handler500'),
    url(r'^events/$', views.Events.as_view(), name='events'),
    url(r'^events/(?P<slug>[-\w]+)/$', views.ViewEvent.as_view(), name='event'),
    url(r'^facts/$', views.Facts.as_view(), name='facts'),
    url(r'^facts/(?P<slug>[-\w]+)/$', views.ViewFact.as_view(), name='fact'),
    url(r'^tag/(?P<slug>[-\w]+)/$', views.TagPosts.as_view(), name='tag'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
