from django import template

register = template.Library()


@register.filter
def total_quantity(items):
    total = 0
    for item in items:
        total += item.quantity
    return total
