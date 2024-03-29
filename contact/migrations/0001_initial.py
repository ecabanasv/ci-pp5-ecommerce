# Generated by Django 3.2 on 2023-04-01 13:18

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Contact",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=100,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="Name can only contain letters and spaces",
                                regex="^[a-zA-Z\\s]+$",
                            )
                        ],
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        max_length=100,
                        validators=[
                            django.core.validators.EmailValidator(
                                code="invalid_email",
                                message="Email is invalid",
                            )
                        ],
                    ),
                ),
                (
                    "subject",
                    models.CharField(
                        max_length=100,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="Subject contains invalid characters",
                                regex="^[a-zA-Z0-9\\s\\-\\_\\.\\,\\!\\?\\']+",
                            )
                        ],
                    ),
                ),
                (
                    "message",
                    models.TextField(
                        max_length=1000,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="Message contains invalid characters",
                                regex="^[^\\n\\r\\t\\f\\v]+$",
                            )
                        ],
                    ),
                ),
            ],
        ),
    ]
