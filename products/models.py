from django.db import models
from django.contrib.auth.models import User

# The Category model represents a category of books


class Category(models.Model):
    # The name of the category
    name = models.SlugField(max_length=100, unique=True)

    # A brief description of the category
    description = models.TextField()

    # A friendly name for the category, to be used in URLs and in the admin interface
    friendly_name = models.CharField(max_length=100, blank=True)

    # Define a string representation for the model
    def __str__(self):
        return self.name

    # A method to get the friendly name for the category
    def get_friendly_name(self):
        return self.friendly_name


# The SubCategory model represents a subcategory of books within a Category
class SubCategory(models.Model):
    # The name of the subcategory
    name = models.SlugField(max_length=100, unique=True)

    # A brief description of the subcategory
    description = models.TextField()

    # A foreign key to the Category model
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='subcategories')

    # A friendly name for the subcategory, to be used in URLs and in the admin interface
    friendly_name = models.CharField(max_length=100, blank=True)

    # Define a string representation for the model
    def __str__(self):
        return self.name

    # A method to get the friendly name for the subcategory
    def get_friendly_name(self):
        return self.friendly_name


class Publisher(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

# The Book model represents a book


class Book(models.Model):
    # ISBN number of the book
    isbn = models.CharField(max_length=100, unique=True)

    # Title of the book
    title = models.CharField(max_length=100)

    # A short description of the book
    small_description = models.CharField(max_length=200, blank=True, null=True)

    # A brief description of the book
    description = models.TextField(blank=True)

    # A foreign key to the Category model
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='books')

    # A foreign key to the SubCategory model
    subcategory = models.ForeignKey(
        SubCategory, on_delete=models.CASCADE, related_name='books')

    # A foreign key to the Publisher model
    publisher = models.ForeignKey(
        Publisher, on_delete=models.CASCADE, related_name='books')

    # A foreign key to the Author model
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, related_name='books')

    # Price of the book
    price = models.DecimalField(max_digits=10, decimal_places=2)

    # Available stock of the book
    stock = models.PositiveIntegerField()

    # Rating of the book
    rating = models.FloatField()

    # Cover image of the book
    cover_image = models.ImageField(upload_to='book_covers/', blank=True, null=True)

    # The publication date of the book
    publication_date = models.DateField(blank=True, null=True)

    # The number of pages in the book
    pages = models.PositiveSmallIntegerField()

    # The language in which the book is written
    language = models.CharField(max_length=100)

    # Define a string representation for the model

    def __str__(self):
        return self.title

class FavoriteBook(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'book')
