# import forms
from django import forms
# import the Contact model
from .models import Contact
# import the FormHelper and Submit classes
from crispy_forms.helper import FormHelper
# import the Submit class
from crispy_forms.layout import Submit
# import the ReCaptchaField class
from captcha.fields import ReCaptchaField

# Create the ContactForm
class ContactForm(forms.ModelForm):
    # add the ReCaptchaField
    captcha = ReCaptchaField()

    class Meta:
        model = Contact
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))
