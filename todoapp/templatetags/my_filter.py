from django import template
from django.db.models import QuerySet

register=template.Library()

@register.filter(name='order')
def order(value:QuerySet ):
    return value.order_by('-id')