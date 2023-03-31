# import the models module from django.db
from django.db import models

# import the User model from django.contrib.auth.models
from django.contrib.auth.models import User

# validators for the fields in the model
from django.core.validators import (
    MinValueValidator,
    MaxValueValidator,
    RegexValidator,
)


# The Category model represents a category of books


class Category(models.Model):
    """Category model"""

    # The name of the category
    name = models.SlugField(
        max_length=100,
        unique=True,
        validators=[
            RegexValidator(
                regex="^[a-z0-9-]+$",
                message="Name must be a slug",
                code="invalid_category_name",
            )
        ],
    )

    # A brief description of the category
    description = models.TextField(
        blank=True,
        null=True,
        validators=[
            RegexValidator(
                regex=r"^[a-zA-Z0-9\s-]+$",
                message="Description contains invalid characters",
                code="invalid_category_description",
            )
        ],
    )

    # A friendly name for the category
    friendly_name = models.CharField(
        max_length=100,
        blank=True,
        validators=[
            RegexValidator(
                regex="^[a-z0-9-]+$",
                message="Friendly name must be alphanumeric",
                code="invalid_category_friendly_name",
            )
        ],
    )

    # Define a string representation for the model

    def __str__(self):
        """String representation of the model"""
        return self.name

    # A method to get the friendly name for the category
    def get_friendly_name(self):
        """Get the friendly name for the category"""
        return self.friendly_name


# The SubCategory model represents a subcategory of books within a Category
class SubCategory(models.Model):
    """Subcategory model"""

    # The name of the subcategory
    name = models.SlugField(
        max_length=100,
        unique=True,
        validators=[
            RegexValidator(
                regex="^[a-z0-9-]+$",
                message="Name must be a slug",
                code="invalid_subcategory_name",
            )
        ],
    )

    # A brief description of the subcategory
    description = models.TextField(
        blank=True,
        null=True,
        validators=[
            RegexValidator(
                regex=r"^[a-zA-Z0-9\s-]+$",
                message="Description contains invalid characters",
                code="invalid_subcategory_description",
            )
        ],
    )

    # A foreign key to the Category model
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="subcategories"
    )

    # A friendly name for the subcategory
    friendly_name = models.CharField(
        max_length=100,
        blank=True,
        validators=[
            RegexValidator(
                regex="^[a-z0-9-]+$",
                message="Friendly name must be alphanumeric",
                code="invalid_subcategory_friendly_name",
            )
        ],
    )

    # Define a string representation for the model

    def __str__(self):
        """String representation of the model"""
        return self.name

    # A method to get the friendly name for the subcategory
    def get_friendly_name(self):
        """Get the friendly name for the subcategory"""
        return self.friendly_name


# The Publisher model represents a publisher of books


class Publisher(models.Model):
    """Publisher model"""

    # The name of the publisher
    name = models.CharField(
        max_length=100,
        unique=True,
        validators=[
            RegexValidator(
                regex=r"^[a-zA-Z\s]*$",
                message="Name must be alphabetic",
                code="invalid_publisher_name",
            )
        ],
    )
    # A brief description of the publisher
    description = models.TextField(
        blank=True,
        validators=[
            RegexValidator(
                regex=r"^[a-zA-Z0-9\s-]+$",
                message="Description contains invalid characters",
                code="invalid_publisher_description",
            )
        ],
    )

    def __str__(self):
        """String representation of the model"""
        return self.name


# The Author model represents an author of books


class Author(models.Model):
    """Author model"""

    # The name of the author
    name = models.CharField(
        max_length=100,
        unique=True,
        validators=[
            RegexValidator(
                regex=r"^[a-zA-Z\s]*$",
                message="Name must be alphabetic",
                code="invalid_author_name",
            )
        ],
    )

    # A brief description of the author
    description = models.TextField(
        blank=True,
        validators=[
            RegexValidator(
                regex=r"^[a-zA-Z0-9\s-]+$",
                message="Description contains invalid characters",
                code="invalid_author_description",
            )
        ],
    )

    def __str__(self):
        """String representation of the model"""
        return self.name


# The Book model represents a book


class Book(models.Model):
    """Book model"""

    # ISBN number of the book
    # regex for isbn-10 and isbn-13
    isbn = models.CharField(
        max_length=13,
        unique=True,
        validators=[
            RegexValidator(
                regex=r"^(978|979)?\d{9}(\d|X)$",
                message="Invalid ISBN",
                code="invalid_isbn",
            )
        ],
    )

    # Title of the book
    title = models.CharField(
        max_length=60,
        validators=[
            RegexValidator(
                regex=r"^[a-zA-Z0-9\s!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~]+$",
                message="Title contains invalid characters",
                code="invalid_title",
            )
        ],
    )

    # A short description of the book
    small_description = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        validators=[
            RegexValidator(
                regex=r"^[a-zA-Z0-9\s-]+$",
                message="Small description contains invalid characters",
                code="invalid_small_description",
            )
        ],
    )

    # A brief description of the book
    description = models.TextField(
        max_length=500,
        blank=True,
        validators=[
            RegexValidator(
                regex=r"^[a-zA-Z0-9\s-]+$",
                message="Description contains invalid characters",
                code="invalid_description",
            )
        ],
    )

    # A foreign key to the Category model
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="books"
    )

    # A foreign key to the SubCategory model
    subcategory = models.ForeignKey(
        SubCategory, on_delete=models.CASCADE, related_name="books"
    )

    # A foreign key to the Publisher model
    publisher = models.ForeignKey(
        Publisher, on_delete=models.CASCADE, related_name="books"
    )

    # A foreign key to the Author model
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, related_name="books"
    )

    # Price of the book
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0), MaxValueValidator(10000)],
    )

    # Available stock of the book
    stock = models.PositiveIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(10000)]
    )

    # Rating of the book
    rating = models.FloatField(
        max_length=2,
        blank=True,
        null=True,
        validators=[MinValueValidator(0), MaxValueValidator(5)],
    )

    # Cover image of the book
    cover_image = models.ImageField(
        upload_to="book_covers/", blank=True, null=True
    )

    # The publication date of the book
    publication_date = models.DateField(blank=True, null=True)

    # The number of pages in the book
    pages = models.PositiveSmallIntegerField(
        blank=True,
        null=True,
        validators=[MinValueValidator(1), MaxValueValidator(10000)],
    )

    # The language in which the book is written
    language = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        validators=[
            RegexValidator(
                regex=r"^[a-zA-Z\s]+$",
                message="Language must be alphabetic",
                code="invalid_language",
            )
        ],
    )

    # Define a string representation for the model

    def __str__(self):
        """String representation of the model"""
        return self.title


# The FavoriteBook model represents a book that a user has favorited


class FavoriteBook(models.Model):
    """FavoriteBook model"""

    # A foreign key to the User model
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # A foreign key to the Book model
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    class Meta:
        """Meta class"""

        unique_together = ("user", "book")
