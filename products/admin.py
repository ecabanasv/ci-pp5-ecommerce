# Import the necessary modules
from django.contrib import admin
from .models import Book, Category, SubCategory, Author, Publisher

# Define a custom ModelAdmin class for the Book model


class BookAdmin(admin.ModelAdmin):
    """Custom ModelAdmin class for the Book model"""

    # Specify the fields that should be displayed in the list view of the model in the admin interface
    list_display = (
        "isbn",
        "title",
        "author",
        "price",
        "rating",
        "stock",
        "category",
        "subcategory",
        "publisher",
    )
    # Specify the fields that can be searched in the list view of the model in the admin interface
    search_fields = ("isbn", "title", "author__name")
    # Specify the fields that can be used to filter the data in the list view of the model in the admin interface
    list_filter = ("category__name", "subcategory__name", "publisher__name")


# Define a custom ModelAdmin class for the Category model


class CategoryAdmin(admin.ModelAdmin):
    """Custom ModelAdmin class for the Category model"""

    # Specify the fields that should be displayed in the list view of the model in the admin interface
    list_display = ("name", "friendly_name", "description")
    # Specify the fields that can be searched in the list view of the model in the admin interface
    search_fields = ("name", "friendly_name")


# Define a custom ModelAdmin class for the SubCategory model


class SubCategoryAdmin(admin.ModelAdmin):
    """Custom ModelAdmin class for the SubCategory model"""

    # Specify the fields that should be displayed in the list view of the model in the admin interface
    list_display = ("name", "friendly_name", "description", "category")
    # Specify the fields that can be searched in the list view of the model in the admin interface
    search_fields = ("name", "friendly_name")
    # Specify the fields that can be used to filter the data in the list view of the model in the admin interface
    list_filter = ("category__name",)


class AuthorAdmin(admin.ModelAdmin):
    """Custom ModelAdmin class for the Author model"""

    list_display = ("name", "description")
    search_fields = ("name",)


class PublisherAdmin(admin.ModelAdmin):
    """Custom ModelAdmin class for the Publisher model"""

    list_display = ("name", "description")
    search_fields = ("name",)


# Register the models with the admin site, using the custom ModelAdmin classes where applicable
admin.site.register(Book, BookAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Publisher, PublisherAdmin)
