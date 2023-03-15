from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Book

def cart_contents(request):
    """ Ensures that the cart contents are available when rendering every page """
    cart_items = []
    total = 0
    product_count = 0
    cart = request.session.get('cart', {})
    for item_id, quantity in cart.items():
        product = get_object_or_404(Book, pk=item_id)
        total += quantity * product.price
        product_count += quantity
        cart_items.append({'item_id': item_id, 'quantity': quantity, 'product': product, 'stock': product.stock})
    
    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0
    
    grand_total = delivery + total

    context = {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'standard_delivery_percentage': settings.STANDARD_DELIVERY_PERCENTAGE,
        'grand_total': grand_total,
    }

    return context