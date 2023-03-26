from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
import requests

from .forms import ContactForm


class ContactView(FormView):
    template_name = 'contact/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact:contact')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['site_key'] = settings.RECAPTCHA_PUBLIC_KEY
        return context

    def get_initial(self):
        initial = super().get_initial()
        if self.request.user.is_authenticated:
            initial['name'] = self.request.user.username
            initial['email'] = self.request.user.email
        return initial

    def form_valid(self, form):
        recaptcha_response = self.request.POST.get('g-recaptcha-response')
        print(recaptcha_response) # recaptcha_response output
        data = {
            'secret': settings.RECAPTCHA_PRIVATE_KEY,
            'response': recaptcha_response
        }
        r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
        result = r.json()
        print(result) # result output
        if not result['success']:
            form.add_error(None, 'Invalid reCAPTCHA')
            return super().form_invalid(form)

        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        subject = form.cleaned_data['subject']
        subject = render_to_string(
            'contact/confirmation_emails/confirmation_email_subject.txt',
            {'subject': subject})
        message = form.cleaned_data['message']
        message = render_to_string(
            'contact/confirmation_emails/confirmation_email_body.txt',
            {'name': name, 'message': message})
        send_mail(
            subject,
            message,
            email,
            [settings.EMAIL_HOST_USER],
            fail_silently=False,
        )
        messages.success(self.request, 'Your message has been sent!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Please correct the errors below.')
        return super().form_invalid(form)

    def get_success_url(self):
        return reverse_lazy('contact:contact')
