# Import the necessary modules
from django.contrib import admin
from .models import Book, Category, SubCategory, Author, Publisher

# Define a custom ModelAdmin class for the Book model


class BookAdmin(admin.ModelAdmin):
    """Custom ModelAdmin class for the Book model"""

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
    search_fields = ("isbn", "title", "author__name")
    list_filter = ("category__name", "subcategory__name", "publisher__name")


# Define a custom ModelAdmin class for the Category model


class CategoryAdmin(admin.ModelAdmin):
    """Custom ModelAdmin class for the Category model"""

    list_display = ("name", "friendly_name", "description")
    search_fields = ("name", "friendly_name")


# Define a custom ModelAdmin class for the SubCategory model


class SubCategoryAdmin(admin.ModelAdmin):
    """Custom ModelAdmin class for the SubCategory model"""

    list_display = ("name", "friendly_name", "description", "category")
    search_fields = ("name", "friendly_name")
    list_filter = ("category__name",)


class AuthorAdmin(admin.ModelAdmin):
    """Custom ModelAdmin class for the Author model"""

    list_display = ("name", "description")
    search_fields = ("name",)


class PublisherAdmin(admin.ModelAdmin):
    """Custom ModelAdmin class for the Publisher model"""

    list_display = ("name", "description")
    search_fields = ("name",)


# Register the models with the admin interface
admin.site.register(Book, BookAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Publisher, PublisherAdmin)
