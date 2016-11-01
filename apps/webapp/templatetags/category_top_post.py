from django import template

from webapp.models import Post, Category

register = template.Library()


@register.inclusion_tag('top_category_post.html')
def get_category_top():
    categories = Category.objects.all()
    posts = list()
    for category in categories:
        posts.append(Post.objects.filter(status='published').filter(category__name=category).order_by('views').last())
    return {'posts': posts}
