from django import template

from webapp.models import Post

register = template.Library()


@register.inclusion_tag('random_advice.html')
def get_random_advice():
    return {'random_advice_posts': Post.objects.filter(status='published').order_by('?')[:4]}
