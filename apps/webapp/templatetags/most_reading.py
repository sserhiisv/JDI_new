from django import template

from webapp.models import Post

register = template.Library()


@register.inclusion_tag('most_reading_posts.html')
def get_most_reading():
    return {'most_read_posts': Post.objects.filter(status='published').order_by('views')[:2]}
