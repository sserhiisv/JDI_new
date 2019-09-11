# -*- coding: utf-8 -*-
import operator

from datetime import datetime

from django.shortcuts import render_to_response, redirect
from django.utils.translation import ugettext_lazy as _
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.db.models import Q

from hitcount.views import HitCountDetailView

from webapp.models import ReadPost, Category, Event, Fact, Tag


class HomePage(ListView):
    template_name = 'main.html'
    model = ReadPost

    def get_context_data(self, **kwargs):
        context = super(HomePage, self).get_context_data(**kwargs)
        context['last_posts'] = ReadPost.objects.filter(status='published') \
                                            .filter(date__lte=datetime.now())[:5]
        context['rand_posts'] = ReadPost.objects.filter(status='published') \
                                            .filter(date__lte=datetime.now()) \
                                            .order_by('?')[:5]
        context['events'] = Event.objects.filter(status='published')[:5]
        context['facts'] = Fact.objects.filter(status='published')[:5]
        return context


class NewPosts(ListView):
    model = ReadPost
    template_name = 'new_posts.html'
    paginate_by = 5
    context_object_name = 'new_posts'

    def get_queryset(self):
        return ReadPost.objects.filter(status='published') \
                           .filter(date__lte=datetime.now())


class PopularPosts(ListView):
    template_name = 'popular_posts.html'
    model = ReadPost

    def get_context_data(self, **kwargs):
        context = super(PopularPosts, self).get_context_data(**kwargs)
        context['pop_posts'] = ReadPost.objects.filter(status='published') \
                                           .filter(date__lte=datetime.now()) \
                                           .order_by('views')[:10]
        return context


class CategoryPosts(ListView):
    template_name = "category_posts.html"
    model = ReadPost
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(CategoryPosts, self).get_context_data(**kwargs)
        context['cat_posts'] = ReadPost.objects.filter(status='published') \
                                           .filter(date__lte=datetime.now()) \
                                           .filter(category__slug=self.kwargs.get('slug'))
        context['category'] = Category.objects.get(slug=self.kwargs.get('slug'))
        return context


class ViewPost(HitCountDetailView):
    model = ReadPost
    template_name = "post.html"
    count_hit = True

    def get_context_data(self, **kwargs):
        context = super(ViewPost, self).get_context_data(**kwargs)
        r_post = ReadPost.objects.get(slug=self.kwargs['slug'])
        context['read_post'] = r_post
        context['similar'] = ReadPost.objects.filter(date__lte=datetime.now()) \
                                         .filter(category=r_post.category) \
                                         .filter(~Q(slug=self.kwargs['slug'])) \
                                         .order_by('?')[:3]
        return context


class Events(ListView):
    model = Event
    template_name = "events.html"
    context_object_name = 'events'
    paginate_by = 10


class ViewEvent(DetailView):
    model = Event
    template_name = "event.html"

    def get_context_data(self, **kwargs):
        context = super(ViewEvent, self).get_context_data(**kwargs)
        context['event'] = Event.objects.get(slug=self.kwargs['slug'])
        return context


class Facts(ListView):
    model = Fact
    template_name = "facts.html"
    context_object_name = 'facts'
    paginate_by = 10


class ViewFact(DetailView):
    model = Fact
    template_name = "fact.html"

    def get_context_data(self, **kwargs):
        context = super(ViewFact, self).get_context_data(**kwargs)
        context['fact'] = Fact.objects.get(slug=self.kwargs['slug'])
        return context


class Room():
    pass


class TagPosts(ListView):
    model = ReadPost
    template_name = "tag.html"

    def get_context_data(self, **kwargs):
        context = super(TagPosts, self).get_context_data(**kwargs)
        context['posts'] = ReadPost.objects.filter(date__lte=datetime.now()) \
                                       .filter(tag__slug=self.kwargs['slug'])
        context['tag'] = Tag.objects.get(slug=self.kwargs['slug'])
        return context


def search(request):
    """
    messages = []
    result = ''
    result_event = ''
    result_fact = ''
    args = {}
    if 'search_phrase' in request.GET and request.GET['search_phrase']:
        try:
            search_phrase = request.GET.get('search_phrase')
            logger.error(search_phrase)
            if not len(search_phrase):
                messages.append(_('Ви не ввели ничего. Пожалуйста, введите данные для поиска.'))
            elif len(search_phrase) > 20:
                messages.append(_('Пожалуйста, введите меньше чем 20 символов.'))
            else:
                result = Post.objects.filter(Q(title__icontains=search_phrase)|Q(content__icontains=search_phrase))
                result_event = Event.objects.filter(Q(title__icontains=search_phrase)|Q(content__icontains=search_phrase))
                result_fact = Fact.objects.filter(Q(title__icontains=search_phrase)|Q(content__icontains=search_phrase))
                if not len(result) and not len(result_event) and not len(result_fact):
                    messages.append(_('Ничего не найдено.'))
        except Exception:
            messages.append(_('Извините. На данный момент поиск не доступен'))
    args['result'] = result
    args['result_event'] = result_event
    args['result_fact'] = result_fact
    args['messages'] = messages
    return render_to_response('search.html', args)
    """
    messages = []
    result = ''
    result_event = ''
    result_fact = ''
    args = {}
    if 'search_phrase' in request.GET and request.GET['search_phrase']:
        try:
            search_phrase = request.GET.get('search_phrase')
            if not len(search_phrase):
                messages.append('You didn\'t enter data. Please, enter a search term.')
            elif len(search_phrase) > 20:
                messages.append('Please enter at most 20 charachters.')
            else:
                result = Post.objects.filter(Q(title__icontains=search_phrase)|Q(content__icontains=search_phrase))
                result_event = Event.objects.filter(Q(title__icontains=search_phrase)|Q(content__icontains=search_phrase))
                result_fact = Fact.objects.filter(Q(title__icontains=search_phrase)|Q(content__icontains=search_phrase))
                if not len(result):
                    messages.append('Sorry, your search returned no matches.')
        except Exception:
            messages.append('Sorry. Search now is not available.')
    args['result'] = result
    args['result_event'] = result_event
    args['result_fact'] = result_fact
    args['messages'] = messages
    args['title_1'] = 'result'
    args['title_2'] = 'results'
    args['count'] = len(result)
    return render_to_response('search.html', args)


def handler404(request):
    return render_to_response('404.html', status=404)


def handler500(request):
    return render_to_response('500.html', status=500)


def about(request):
    return render_to_response('about.html')
