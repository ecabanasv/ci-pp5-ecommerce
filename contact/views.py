# shortcuts is used to render the template
from django.shortcuts import render, redirect
# import the ContactForm
from .forms import ContactForm
# import messages
from django.contrib import messages
# import the send_mail function
from django.core.mail import send_mail
# import the View class
from django.views import generic, View
# render_to_string is used to render the email template
from django.template.loader import render_to_string
# settings is used to get the email settings
from django.conf import settings
# import the View class
from django.views.generic import View

# Create your views here.

# Contact View
class ContactView(View):
    def get(self, request):
        # get the ContactForm
        form = ContactForm()
        # render the template
        return render(request, 'contact/contact.html', {'form': form})

    def post(self, request):
        # get the ContactForm
        form = ContactForm(request.POST)
        # check if the form is valid
        if form.is_valid():
            # get the data from the form
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            subject = render_to_string(
                'contact/confirmation_emails/confirmation_email_subject.txt',
                {'subject': subject})
            message = form.cleaned_data['message']
            message = render_to_string(
                'contact/confirmation_emails/confirmation_email_body.txt',
                {'name': name , 'message': message})
            # send the email
            send_mail(
                subject,
                # message
                message,
                # from email
                email,
                # to email
                [settings.EMAIL_HOST_USER],
                # fail_silently
                fail_silently=False,
            )
            # create a success message
            messages.success(request, 'Your message has been sent!')
            # redirect to the contact page
            return redirect('contact:contact')

        # if the form is not valid
        else:
            # create an error message
            messages.error(request, 'Please correct the errors below.')
            # render the template
            return render(request, 'contact/contact.html', {'form': form}) 
    


