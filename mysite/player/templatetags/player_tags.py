from django import template
from  ..models import Player

register = template.Library()


@register.filter(name='lookup')
def lookup(value, arg):
    return value[arg]


@register.filter(name='in')
def lookup(value, arg):
    return arg in value


@register.filter(name='myformat')
def myformat(value):
    return int(value) if value.is_integer() else round(value, 2)