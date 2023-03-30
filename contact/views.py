# reverse_lazy is used to avoid circular imports
from django.urls import reverse_lazy

# FormView is used to display a form
from django.views.generic import FormView

# messages is used to display messages to the user
from django.contrib import messages

# send_mail is used to send emails
from django.core.mail import send_mail

# render_to_string is used to render a template to a string
from django.template.loader import render_to_string

# settings is used to access the settings.py file
from django.conf import settings

# Import the form
from .forms import ContactForm


# class ContactView is used to display the contact form
class ContactView(FormView):
    """A view to display the contact form"""
    # The template to be used
    template_name = "contact/contact.html"
    # The form to be used
    form_class = ContactForm
    # The url to redirect to after the form is submitted
    success_url = reverse_lazy("contact:contact")

    # get_context_data is used to pass data to the template
    def get_context_data(self, **kwargs):
        """Pass data to the template"""
        context = super().get_context_data(**kwargs)
        return context

    # get_initial is used to set the initial values of the form
    def get_initial(self):
        """Set the initial values of the form"""
        initial = super().get_initial()
        if self.request.user.is_authenticated:
            initial["name"] = self.request.user.username
            initial["email"] = self.request.user.email
        return initial

    # form_valid is used to send the email
    def form_valid(self, form):
        """Send the email"""
        name = form.cleaned_data["name"]
        email = form.cleaned_data["email"]
        subject = form.cleaned_data["subject"]
        subject = render_to_string(
            "contact/confirmation_emails/confirmation_email_subject.txt",
            {"subject": subject},
        )
        message = form.cleaned_data["message"]
        message = render_to_string(
            "contact/confirmation_emails/confirmation_email_body.txt",
            {"name": name, "message": message},
        )
        send_mail(
            subject,
            message,
            email,
            [settings.EMAIL_HOST_USER],
            fail_silently=False,
        )
        messages.success(self.request, "Your message has been sent!")
        return super().form_valid(form)

    # form_invalid is used to display an error message
    def form_invalid(self, form):
        """Display an error message"""
        messages.error(self.request, "Please correct the errors below.")
        return super().form_invalid(form)

    # get_success_url is used to redirect to the success url
    def get_success_url(self):
        """Redirect to the success url"""
        return reverse_lazy("contact:contact")
