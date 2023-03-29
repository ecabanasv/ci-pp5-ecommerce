# import admin from django.contrib
from django.contrib import admin

# import Contact
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    # List Display
    list_display = ("id", "name", "email", "subject", "message")
    # List Display Links
    list_display_links = ("id", "subject")
    # Search Fields
    search_fields = ("name", "email", "subject", "message")
    # List Per Page
    list_per_page = 25


# Register Contact
admin.site.register(Contact, ContactAdmin)
