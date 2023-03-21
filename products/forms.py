from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from django import forms
from .models import Book, Category, SubCategory, Publisher, Author

# class BookForm(forms.ModelForm):

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        labels = {
            'isbn': 'ISBN',
            'small_description': 'Short Description',
            'publication_date': 'Publication Date (YYYY-MM-DD)',
            'cover_image': 'Cover Image (JPG or PNG)',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save'))


# class BookUpdateForm(forms.ModelForm):

class BookUpdateForm(forms.ModelForm):
    class Meta:
        model = Book
        template_name = 'products/book_form.html'
        fields = '__all__'
        labels = {
            'isbn': 'ISBN',
            'small_description': 'Short Description',
            'publication_date': 'Publication Date (YYYY-MM-DD)',
            'cover_image': 'Cover Image (JPG or PNG)',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save'))


# class CategoryForm(forms.ModelForm):

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        labels = {
            'name': 'Category Name',
            'description': 'Description',
            'friendly_name': 'Friendly Name',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save'))

# class CategoryUpdateForm(forms.ModelForm):

class CategoryUpdateForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        labels = {
            'name': 'Category Name',
            'description': 'Description',
            'friendly_name': 'Friendly Name',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save'))


# class SubCategoryForm(forms.ModelForm):

class SubCategoryForm(forms.ModelForm):
    class Meta:
        model = SubCategory
        fields = '__all__'
        labels = {
            'name': 'Subcategory Name',
            'description': 'Description',
            'category': 'Category',
            'friendly_name': 'Friendly Name',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save'))


# class SubCategoryUpdateForm(forms.ModelForm):

class SubCategoryUpdateForm(forms.ModelForm):
    class Meta:
        model = SubCategory
        fields = '__all__'
        labels = {
            'name': 'Subcategory Name',
            'description': 'Description',
            'category': 'Category',
            'friendly_name': 'Friendly Name',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save'))


# class PublisherForm(forms.ModelForm):

class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = '__all__'
        labels = {
            'name': 'Publisher Name',
            'description': 'Description',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save'))


# c;ass PublisherUpdateForm(forms.ModelForm):

class PublisherUpdateForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = '__all__'
        labels = {
            'name': 'Publisher Name',
            'description': 'Description',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save'))


# class AuthorForm(forms.ModelForm):

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'
        labels = {
            'name': 'Author Name',
            'description': 'Description',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save'))


# class AuthorUpdateForm(forms.ModelForm):

class AuthorUpdateForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'
        labels = {
            'name': 'Author Name',
            'description': 'Description',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save'))