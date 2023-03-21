# shortcuts is used to render templates and get objects or return a 404 error
from django.shortcuts import render, get_object_or_404
# messages is used to display messages to the user
from django.contrib import messages
# login_required is a decorator that checks if the user is logged in
from django.contrib.auth.decorators import login_required

# Import the models
from .models import UserProfile
from checkout.models import Order

# Import the form
from .forms import UserProfileForm

# profile view
# @login_required is a decorator that checks if the user is logged in

@login_required
def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')

    form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True
    }

    return render(request, template, context)


# order_history view
# @login_required is a decorator that checks if the user is logged in

@login_required
def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)