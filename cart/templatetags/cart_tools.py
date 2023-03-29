# template tag to calculate the subtotal
# of a product in the cart
from django import template

# register the template tag as a filter
register = template.Library()


# define the filter
@register.filter(name="calc_subtotal")
def calc_subtotal(price, quantity):
    return price * quantity
