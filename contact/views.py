# shortcuts is used to render the template
from django.shortcuts import render
# import the ContactForm
from .forms import ContactForm
# import messages
from django.contrib import messages
# import the View class
from django.views.generic import View

# Create your views here.

# Contact View
class ContactView(View):
    # Contact Form
    form = ContactForm
    # Contact Template
    template_name = 'contact/contact.html'

    # Get Contact Form
    def get(self, request):
        # Get the form
        form = self.form()
        # Render the template
        return render(request, self.template_name, {'form': form})
    
    # Post Contact Form
    def post(self, request):
        # Get the form
        form = self.form(request.POST)
        # Check if the form is valid
        if form.is_valid():
            contact = form.save()
            contact.save()
            # Send a success message
            messages.success(request, 'Your message has been sent!')
            # Redirect to the home page
            return render(request, 'home/index.html')
        else:
            # Send an error message
            messages.error(request, 'Please correct the error below.')
            # Redirect to the home page
            return render(request, 'contact/contact.html', {'form': form})

