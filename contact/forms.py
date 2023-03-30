# forms imports
from django import forms
# Import the model
from .models import Contact
# Import the helper
from crispy_forms.helper import FormHelper
# Import the submit button
from crispy_forms.layout import Submit


# Create the form class
class ContactForm(forms.ModelForm):
    """A form to contact the site owner"""
    # The Meta class is used to set the model and fields
    class Meta:
        """Meta class"""
        model = Contact
        fields = '__all__'

    # __init__ is used to set the form helper
    def __init__(self, *args, **kwargs):
        """Set the form helper"""
        super(ContactForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))
