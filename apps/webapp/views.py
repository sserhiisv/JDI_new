from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.db.models import Q

from webapp.models import Post, Category, Event, Fact, Tag


class HomePage(ListView):
    template_name = 'main.html'
    model = Post

    def get_context_data(self, **kwargs):
        context = super(HomePage, self).get_context_data(**kwargs)
        context['last_posts'] = Post.objects.filter(status='published')[:5]
        context['rand_posts'] = Post.objects.filter(status='published').order_by('?')[:5]
        context['events'] = Event.objects.filter(status='published')[:5]
        context['facts'] = Fact.objects.filter(status='published')[:5]
        return context


class NewPosts(ListView):
    model = Post
    template_name = 'new_posts.html'

    def get_context_data(self, **kwargs):
        context = super(NewPosts, self).get_context_data(**kwargs)
        context['new_posts'] = Post.objects.filter(status='published')[:5]
        context['new_events'] = Event.objects.filter(status='published')[:5]
        context['new_facts'] = Fact.objects.filter(status='published')[:5]
        return context


class PopularPosts(ListView):
    template_name = 'popular_posts.html'
    model = Post

    def get_context_data(self, **kwargs):
        context = super(PopularPosts, self).get_context_data(**kwargs)
        context['pop_posts'] = Post.objects.filter(status='published').order_by('-views')[:10]
        return context


class CategoryPosts(ListView):
    template_name = "category_posts.html"
    model = Post
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(CategoryPosts, self).get_context_data(**kwargs)
        context['cat_posts'] = Post.objects.filter(status='published').filter(category__slug=self.kwargs.get('slug')).order_by('-views')
        context['category'] = Category.objects.get(slug=self.kwargs.get('slug'))
        return context


class ViewPost(DetailView):
    model = Post
    template_name = "post.html"

    def get_context_data(self, **kwargs):
        context = super(ViewPost, self).get_context_data(**kwargs)
        post = Post.objects.get(slug=self.kwargs['slug'])
        context['post'] = post
        context['similar'] = Post.objects.filter(category=post.category).filter(~Q(slug=self.kwargs['slug'])).order_by('?')[:6]
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
    model = Post
    template_name = "tag.html"

    def get_context_data(self, **kwargs):
        context = super(TagPosts, self).get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(tag__slug=self.kwargs['slug'])
        context['tag'] = Tag.objects.get(slug=self.kwargs['slug'])
        return context
