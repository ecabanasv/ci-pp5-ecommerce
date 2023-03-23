from django.shortcuts import render, redirect, get_object_or_404, reverse, HttpResponse
from django.contrib import messages
from products.models import Book


def view_cart(request):
    """ Renders the cart page """

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Adds a specified quantity of a product to the cart """

    product = get_object_or_404(Book, pk=item_id)
    if (request.GET.get('quantity')):
        quantity = int(request.GET.get('quantity'))
    else:
        quantity = 1

    if (request.POST.get('quantity')):
        quantity = int(request.POST.get('quantity'))
    else:
        quantity = 1

    redirect_url = request.GET.get('redirect_url') or 'products:book_list'
    cart = request.session.get('cart', {})

    current_quantity = cart.get(str(item_id), 0)
    total_quantity = current_quantity + quantity

    if total_quantity > product.stock:
        messages.error(request, f'Sorry, we only have {product.stock} units of {product.title} in stock. Please adjust the quantity.')
        return redirect(redirect_url)

    if str(item_id) in list(cart.keys()):
        cart[str(item_id)] += quantity
        messages.success(request, f'Successfully updated the quantity of {product.title} to {cart[str(item_id)]}', extra_tags='added_to_cart')
    else:
        cart[str(item_id)] = quantity
        messages.success(request, f'Successfully added {product.title} to your cart', extra_tags='added_to_cart')

    request.session['cart'] = cart
    request.session.save()
    return redirect(redirect_url)



def adjust_cart(request, item_id):
    """ Adjusts the quantity of a specified product to the specified amount """

    product = get_object_or_404(Book, pk=item_id)
    quantity_str = request.POST.get('quantity', '')
    
    if quantity_str == '':
        quantity = 0
    else:
        quantity = int(quantity_str)

    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[str(item_id)] = quantity
        messages.success(
            request, f'Successfully updated the quantity of {product.title} to {cart[str(item_id)]}')
    else:
        cart.pop(str(item_id))
        messages.success(
            request, f'Successfully removed {product.title} from your cart')

    request.session['cart'] = cart
    request.session.save()  # Save the session explicitly
    return redirect(reverse('cart:view_cart'))




def remove_from_cart(request, item_id):
    """ Remove the item from the shopping bag """
    try:
        product = get_object_or_404(Book, pk=item_id)
        print(f'Product found: {product.title}')  # Debugging statement

        cart = request.session.get('cart', {})
        print(f'Current cart: {cart}')  # Debugging statement

        if str(item_id) in cart:  # Check if item_id exists in the cart
            cart.pop(str(item_id))
            messages.success(
                request, f'Removed {product.title} from your cart')
        else:
            messages.error(
                request, f'Item {product.title} not found in your cart')

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        print(f'Error occurred: {e}')  # Debugging statement
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
