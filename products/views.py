from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Book

# The search_books function displays a list of books based on the search term

def search_books(request):
    queryset = Book.objects.all()
    # Get the search term from the GET request
    search_term = request.GET.get('search', '')
    # Filter the queryset based on the search term
    if search_term:
        queryset = queryset.filter(
            Q(isbn__icontains=search_term) |
            Q(title__icontains=search_term) |
            Q(author__name__icontains=search_term)
        )
    # Paginate the queryset
    paginator = Paginator(queryset, 6)
    page = request.GET.get('page')
    books = paginator.get_page(page)
    # Return the search results as a JSON response
    if request.is_ajax():
        books_data = [{'pk': book.pk, 'title': book.title, 'author': book.author.name, 'isbn': book.isbn, 'cover_image': book.cover_image.url} for book in books]
        return JsonResponse({'books': books_data})
    else:
        return render(request, 'products/book_list.html', {'books': books})


# The BookListView displays a list of books


class BookListView(ListView):
    # Specify the model to use
    model = Book
    # Specify the template name to use
    template_name = 'products/book_list.html'
    # Specify the name of the object to be passed to the template
    context_object_name = 'books'
    # Specify the default sorting order for the books
    ordering = ['title']
    # Specify the number of books to be displayed per page
    paginate_by = 6

    def get_queryset(self):
        queryset = super().get_queryset()
        # Get the sort order from the GET request
        sort_order = self.request.GET.get('sort', 'title')
        sort_direction = self.request.GET.get('direction', 'asc')

        # Order the queryset based on the sort order and direction
        if sort_order == 'title':
            queryset = queryset.order_by('title')
            if sort_direction == 'desc':
                queryset = queryset.reverse()
        elif sort_order == 'price':
            queryset = queryset.order_by('price')
            if sort_direction == 'desc':
                queryset = queryset.reverse()
        elif sort_order == 'rating':
            queryset = queryset.order_by('rating')
            if sort_direction == 'desc':
                queryset = queryset.reverse()
        # Get the category from the GET request
        category = self.request.GET.get('category')
        # Filter the queryset based on the category
        if category:
            queryset = queryset.filter(category__name=category)
        # Get the search term from the GET request
        search_term = self.request.GET.get('search', '')
        # Filter the queryset based on the search term
        if search_term:
            queryset = queryset.filter(
                Q(isbn__icontains=search_term) |
                Q(title__icontains=search_term) |
                Q(author__name__icontains=search_term)
            )
        # Return the filtered and ordered queryset
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add the sort order, search term, and category filter to the context
        context['sort'] = self.request.GET.get('sort', 'title')
        context['direction'] = self.request.GET.get('direction', 'asc')
        context['search'] = self.request.GET.get('search', '')
        context['category'] = self.request.GET.get('category', '')
        # Paginate the books
        paginator = Paginator(self.get_queryset(), self.paginate_by)
        page = self.request.GET.get('page')
        books = paginator.get_page(page)
        context['books'] = books
        return context


# The BookDetailView displays the details of a specific book


class BookDetailView(DetailView):
    # Specify the model to use
    model = Book
    # Specify the template name to use
    template_name = 'products/book_detail.html'

# The BookCreateView allows the user to create a new book


class BookCreateView(CreateView):
    # Specify the model to use
    model = Book
    # Specify the template name to use
    template_name = 'products/book_form.html'
    # Specify the fields to be included in the form
    fields = ['isbn', 'title', 'small_description', 'description', 'author', 'price',
              'rating', 'stock', 'cover', 'category', 'subcategory', 'publication_date', 'publisher', 'pages', 'language']

    # Override the form_valid method to set the author field to the currently logged in user
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# The BookUpdateView allows the user to update the details of a specific book


class BookUpdateView(UpdateView):
    # Specify the model to use
    model = Book
    # Specify the template name to use
    template_name = 'products/book_form.html'
    # Specify the fields to be included in the form
    fields = ['isbn', 'title', 'small_description', 'description', 'author', 'price',
              'rating', 'stock', 'cover', 'category', 'subcategory', 'publication_date', 'publisher', 'pages', 'language']

# The BookDeleteView allows the user to delete a specific book


class BookDeleteView(DeleteView):
    # Specify the model to use
    model = Book
    # Specify the template name to use
    template_name = 'products/book_confirm_delete.html'
    # Specify the URL to redirect to after a successful deletion
    success_url = '/books/'
