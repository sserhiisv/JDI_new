from django import template

from webapp.models import Event, Fact

register = template.Library()


@register.inclusion_tag('new_events_facts.html')
def get_new_events_facts():
    new_events = Event.objects.filter(status='published')[:5]
    new_facts = Fact.objects.filter(status='published')[:5]
    return {'new_events': new_events, 'new_facts': new_facts}
