from django import forms
from .models import Contact
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox
from django.conf import settings


class ContactForm(forms.ModelForm):
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox(
        attrs={
            'data-theme': 'light',
        }
    ))


    class Meta:
        model = Contact
        fields = ('__all__')

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))