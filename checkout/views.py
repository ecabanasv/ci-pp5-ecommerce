from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm

# Create your views here.

def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "There's nothing in your cart at the moment")
        return redirect(reverse('products'))
    
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51Mm2fiDuH2LrwWaVqb8KTvN3oiyZtAKTK5WohgOboFS7QAajSXCB8NbJrjrgmVmaV2c2M7IRrObfFaV4ETwv2af500WdeK6LMZ',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
    
