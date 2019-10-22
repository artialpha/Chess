from django import template
from  ..models import Player

register = template.Library()


@register.filter(name='lookup')
def lookup(value, arg):
    return value[arg]