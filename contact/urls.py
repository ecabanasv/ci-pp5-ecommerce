# path to this file: contact\urls.py
from django.urls import path

# Import the view
from .views import ContactView

# Set the app_name
app_name = "contact"

# Set the urlpatterns
urlpatterns = [
    path("", ContactView.as_view(), name="contact"),
]
