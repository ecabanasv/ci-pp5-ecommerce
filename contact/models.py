# import the models module from django.db
from django.db import models
# import the RegexValidator and EmailValidator
from django.core.validators import RegexValidator, EmailValidator


# The Contact model represents a contact form submission
class Contact(models.Model):
    # The name of the person submitting the contact form
    name = models.CharField(
        max_length=100,
        validators=[
            RegexValidator(
                regex=r'^[a-zA-Z\s]+$',
                message='Name can only contain letters and spaces'
            )
        ]
    )
    # The email address of the person submitting the contact form
    email = models.EmailField(
        max_length=100,
        validators=[
            EmailValidator(
                message='Email is invalid',
                code='invalid_email'
            )
        ]
    )
    # The subject of the contact form submission
    subject = models.CharField(
        max_length=100,
        validators=[
            RegexValidator(
                regex=r'^[a-zA-Z0-9\s\-\_\.\,\!\?\']+',
                message='Subject can only contain letters, numbers, and common punctuation marks'
            )
        ]
    )
    # The message of the contact form submission
    message = models.TextField(max_length=1000,
        validators=[
            RegexValidator(
                regex=r'^[^\n\r\t\f\v]+$',
                message='Message contains invalid characters'
            )
        ]
    )

    # A method to return the name of the contact form submission
    def __str__(self):
        return self.name
