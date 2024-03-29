# forms for the products app
from django import forms

# Formhelper for crispy forms
from crispy_forms.helper import FormHelper

# Submit button for crispy forms
from crispy_forms.layout import Submit

# Import the models
from .models import Book, Category, SubCategory, Publisher, Author


# class BookForm(forms.ModelForm):


class BookForm(forms.ModelForm):
    """Form for the Book model"""

    class Meta:
        # The model to use
        model = Book

        # The fields to use
        fields = "__all__"

        Author = forms.ModelChoiceField(
            queryset=Author.objects.all(), empty_label="Select Author"
        )
        Publisher = forms.ModelChoiceField(
            queryset=Publisher.objects.all(), empty_label="Select Publisher"
        )
        Category = forms.ModelChoiceField(
            queryset=Category.objects.all(), empty_label="Select Category"
        )
        SubCategory = forms.ModelChoiceField(
            queryset=SubCategory.objects.all(),
            empty_label="Select SubCategory",
        )

        labels = {
            "isbn": "ISBN",
            "title": "Title",
            "small_description": "Short Description",
            "description": "Description",
            "author": "Author",
            "price": "Price",
            "rating": "Rating",
            "stock": "Stock",
            "cover_image": "Cover Image",
            "category": "Category",
            "subcategory": "Subcategory",
            "publication_date": "Publication Date",
            "publisher": "Publisher",
            "pages": "Pages",
            "language": "Language",
        }
        # Add placeholders and classes, remove auto-generated
        widgets = {
            "isbn": forms.TextInput(
                attrs={
                    "placeholder": "ISBN-13 or ISBN-10",
                    "minlength": 10,
                    "maxlength": 13,
                    "required": "required",
                }
            ),
            "title": forms.TextInput(
                attrs={
                    "placeholder": "Title",
                    "maxlength": 100,
                    "required": "required",
                }
            ),
            "small_description": forms.Textarea(
                attrs={
                    "placeholder": "Short Description",
                    "maxlength": 200,
                    "rows": 2,
                    "cols": 40,
                    "required": "required",
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "placeholder": "Description",
                    "rows": 4,
                    "cols": 40,
                    "maxlength": 1000,
                }
            ),
            "author": forms.TextInput(
                attrs={"placeholder": "Author", "required": "required"}
            ),
            "price": forms.NumberInput(
                attrs={
                    "placeholder": "Price",
                    "step": "0.01",
                    "min": "0",
                    "max": "100000",
                    "required": "required",
                }
            ),
            "rating": forms.NumberInput(
                attrs={
                    "placeholder": "Rating",
                    "step": "0.1",
                    "min": "0",
                    "max": "5",
                    "required": "required",
                }
            ),
            "stock": forms.NumberInput(
                attrs={
                    "placeholder": "Stock",
                    "step": "1",
                    "max": "100",
                    "min": "0",
                    "value": "0",
                    "required": "required",
                }
            ),
            "cover_image": forms.ClearableFileInput(
                attrs={"accept": "image/*"}
            ),
            "category": forms.TextInput(attrs={"placeholder": "Category"}),
            "subcategory": forms.TextInput(
                attrs={"placeholder": "Subcategory"}
            ),
            "publication_date": forms.DateInput(
                attrs={
                    "type": "date",
                    "required": "required",
                }
            ),
            "publisher": forms.TextInput(attrs={"placeholder": "Publisher"}),
            "pages": forms.NumberInput(
                attrs={
                    "step": "1",
                    "min": 0,
                    "max": 5000,
                    "placeholder": "Pages",
                    "required": "required",
                }
            ),
            "language": forms.TextInput(
                attrs={
                    "placeholder": "Language",
                    "maxlength": 20,
                    "minlength": 2,
                    "required": "required",
                }
            ),
        }

    # Override the init method to add the crispy forms helper
    def __init__(self, *args, **kwargs):
        """Add crispy forms helper to the form"""
        super().__init__(*args, **kwargs)
        self.fields["author"].widget = forms.Select(
            choices=[
                (author.id, author.name) for author in Author.objects.all()
            ]
        )
        self.fields["publisher"].widget = forms.Select(
            choices=[
                (publisher.id, publisher.name)
                for publisher in Publisher.objects.all()
            ]
        )
        self.fields["category"].widget = forms.Select(
            choices=[
                (category.id, category.friendly_name)
                for category in Category.objects.all()
            ]
        )
        self.fields["subcategory"].widget = forms.Select(
            choices=[
                (subcategory.id, subcategory.friendly_name)
                for subcategory in SubCategory.objects.all()
            ]
        )
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.add_input(Submit("submit", "Save"))


# class BookUpdateForm(forms.ModelForm):


class BookUpdateForm(forms.ModelForm):
    """Form for updating a book"""

    class Meta:
        # The model to use
        model = Book

        # The fields to use
        fields = "__all__"

        Author = forms.ModelChoiceField(
            queryset=Author.objects.all(), empty_label="Select Author"
        )
        Publisher = forms.ModelChoiceField(
            queryset=Publisher.objects.all(), empty_label="Select Publisher"
        )
        Category = forms.ModelChoiceField(
            queryset=Category.objects.all(), empty_label="Select Category"
        )
        SubCategory = forms.ModelChoiceField(
            queryset=SubCategory.objects.all(),
            empty_label="Select SubCategory",
        )

        labels = {
            "isbn": "ISBN",
            "title": "Title",
            "small_description": "Short Description",
            "description": "Description",
            "author": "Author",
            "price": "Price",
            "rating": "Rating",
            "stock": "Stock",
            "cover_image": "Cover Image",
            "category": "Category",
            "subcategory": "Subcategory",
            "publication_date": "Publication Date",
            "publisher": "Publisher",
            "pages": "Pages",
            "language": "Language",
        }

        widgets = {
            "isbn": forms.TextInput(
                attrs={
                    "placeholder": "ISBN-13 or ISBN-10",
                    "minlength": 10,
                    "maxlength": 13,
                    "required": "required",
                }
            ),
            "title": forms.TextInput(
                attrs={
                    "placeholder": "Title",
                    "maxlength": 100,
                    "required": "required",
                }
            ),
            "small_description": forms.Textarea(
                attrs={
                    "placeholder": "Short Description",
                    "maxlength": 200,
                    "rows": 2,
                    "cols": 40,
                    "required": "required",
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "placeholder": "Description",
                    "rows": 4,
                    "cols": 40,
                    "maxlength": 1000,
                }
            ),
            "author": forms.TextInput(
                attrs={"placeholder": "Author", "required": "required"}
            ),
            "price": forms.NumberInput(
                attrs={
                    "placeholder": "Price",
                    "step": "0.01",
                    "min": "0",
                    "max": "100000",
                    "required": "required",
                }
            ),
            "rating": forms.NumberInput(
                attrs={
                    "placeholder": "Rating",
                    "step": "0.1",
                    "min": "0",
                    "max": "5",
                    "required": "required",
                }
            ),
            "stock": forms.NumberInput(
                attrs={
                    "placeholder": "Stock",
                    "step": "1",
                    "max": "100",
                    "min": "0",
                    "required": "required",
                }
            ),
            "cover_image": forms.ClearableFileInput(
                attrs={"accept": "image/*"}
            ),
            "category": forms.TextInput(attrs={"placeholder": "Category"}),
            "subcategory": forms.TextInput(
                attrs={"placeholder": "Subcategory"}
            ),
            "publication_date": forms.DateInput(
                attrs={
                    "type": "date",
                    "required": "required",
                }
            ),
            "publisher": forms.TextInput(attrs={"placeholder": "Publisher"}),
            "pages": forms.NumberInput(
                attrs={
                    "step": "1",
                    "min": 0,
                    "max": 5000,
                    "placeholder": "Pages",
                    "required": "required",
                }
            ),
            "language": forms.TextInput(
                attrs={
                    "placeholder": "Language",
                    "maxlength": 20,
                    "minlength": 2,
                    "required": "required",
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        """Initialise the form"""
        super().__init__(*args, **kwargs)
        self.fields["author"].widget = forms.Select(
            choices=[
                (author.id, author.name) for author in Author.objects.all()
            ]
        )
        self.fields["publisher"].widget = forms.Select(
            choices=[
                (publisher.id, publisher.name)
                for publisher in Publisher.objects.all()
            ]
        )
        self.fields["category"].widget = forms.Select(
            choices=[
                (category.id, category.friendly_name)
                for category in Category.objects.all()
            ]
        )
        self.fields["subcategory"].widget = forms.Select(
            choices=[
                (subcategory.id, subcategory.friendly_name)
                for subcategory in SubCategory.objects.all()
            ]
        )
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.add_input(Submit("submit", "Save"))
