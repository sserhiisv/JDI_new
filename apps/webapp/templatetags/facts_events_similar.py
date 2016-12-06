from django import template

from webapp.models import Event, Fact

register = template.Library()


@register.inclusion_tag('event_fact_similar.html')
def event_fact_similar():
    events = Event.objects.filter(status='published')[:5]
    facts = Fact.objects.filter(status='published')[:5]
    return {'events': events, 'facts': facts}
