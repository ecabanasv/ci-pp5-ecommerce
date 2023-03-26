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
# recaptcha
from captcha.fields import ReCaptchaField

# Create your views here.

# Contact View


class ContactView(View):
    def get(self, request):
        # Create a new instance of the ContactForm
        form = ContactForm()
        # Render the contact.html template and pass in the ContactForm and reCAPTCHA site key as context
        return render(request, 'contact/contact.html', {'form': form, 'site_key': settings.RECAPTCHA_PUBLIC_KEY})

    def post(self, request):
        # Create a new instance of the ContactForm with the POST data
        form = ContactForm(request.POST)
        # Check if the form is valid
        if form.is_valid():
            # Verify the user's reCAPTCHA response
            captcha = ReCaptchaField()
            if not captcha.validate(form.cleaned_data.get('captcha')):
                # If the reCAPTCHA response is invalid, add an error to the form and render the contact.html template again
                form.add_error(None, 'Invalid reCAPTCHA')
                return render(request, 'contact/contact.html', {'form': form, 'site_key': settings.RECAPTCHA_PUBLIC_KEY})
            # If the reCAPTCHA response is valid, extract the form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            # Render the email subject line as a template
            subject = render_to_string(
                'contact/confirmation_emails/confirmation_email_subject.txt',
                {'subject': subject})
            message = form.cleaned_data['message']
            # Render the email body as a template
            message = render_to_string(
                'contact/confirmation_emails/confirmation_email_body.txt',
                {'name': name, 'message': message})
            # Send the email using Django's built-in send_mail function
            send_mail(
                subject,
                message,
                email,
                [settings.EMAIL_HOST_USER],
                fail_silently=False,
            )
            # If the email is sent successfully, add a success message to the user's session
            messages.success(request, 'Your message has been sent!')
            # Redirect the user back to the contact page
            return redirect('contact:contact')
        else:
            # If the form is not valid, add an error message to the user's session and render the contact.html template again
            messages.error(request, 'Please correct the errors below.')
            return render(request, 'contact/contact.html', {'form': form, 'site_key': settings.RECAPTCHA_PUBLIC_KEY})
