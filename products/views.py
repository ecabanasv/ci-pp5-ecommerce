"""Views for the products app"""

# JsonResponse is used to return a JSON response
from django.http import JsonResponse

# shortcuts is used to render templates and redirect to URLs
from django.shortcuts import render, redirect, get_object_or_404

# staff_member_required for checks if the user is a staff member
from django.contrib.admin.views.decorators import staff_member_required

# reverse_lazy is used to reverse URLs
from django.urls import reverse_lazy

# method_decorator is used to apply decorators to class-based views
from django.utils.decorators import method_decorator

# login_required is a decorator that checks if the user is logged in
from django.contrib.auth.decorators import login_required

# Import the following generic views
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

# Paginator is used to paginate the queryset
from django.core.paginator import Paginator

# messages is used to display messages to the user
from django.contrib import messages

# Q is used to combine multiple queries
from django.db.models import Q

# Count is used to count the number of items in a query
from django.db.models import Count

# escape is used to escape HTML characters
from django.utils.html import escape

# The following imports are used to create a formset
from .models import Book, FavoriteBook, SubCategory

# The following imports are used to create a formset
from .forms import BookForm, BookUpdateForm

# The search_books function displays a list of books based on the search term


def search_books(request):
    """Search for books"""
    queryset = Book.objects.all()
    # Get the search term from the GET request
    search_term = request.GET.get("search", "")
    # Filter the queryset based on the search term
    if search_term:
        queryset = queryset.filter(
            Q(isbn__icontains=search_term)
            | Q(title__icontains=search_term)
            | Q(author__name__icontains=search_term)
        )
    # Paginate the queryset
    paginator = Paginator(queryset, 6)
    page = request.GET.get("page")
    books = paginator.get_page(page)
    # Return the search results as a JSON response
    if request.is_ajax():
        books_data = [
            {
                "pk": book.pk,
                "title": book.title,
                "author": book.author.name,
                "isbn": book.isbn,
                "cover_image": book.cover_image.url,
            }
            for book in books
        ]
        return JsonResponse({"books": books_data})
    else:
        return render(request, "products/book_list.html", {"books": books})


# The BookListView displays a list of books


class BookListView(ListView):
    """Display a list of books"""

    # Specify the model to use
    model = Book
    # Specify the template name to use
    template_name = "products/book_list.html"
    # Specify the name of the object to be passed to the template
    context_object_name = "books"
    # Specify the default sorting order for the books
    ordering = ["title"]
    # Specify the number of books to be displayed per page
    paginate_by = 6

    def get_queryset(self):
        """Return the queryset"""
        queryset = super().get_queryset()
        # Get the sort order from the GET request
        sort_order = self.request.GET.get("sort", "title")
        sort_direction = self.request.GET.get("direction", "asc")

        # Order the queryset based on the sort order and direction
        if sort_order == "title":
            queryset = queryset.order_by("title")
            if sort_direction == "desc":
                queryset = queryset.reverse()
        elif sort_order == "price":
            queryset = queryset.order_by("price")
            if sort_direction == "desc":
                queryset = queryset.reverse()
        elif sort_order == "rating":
            queryset = queryset.order_by("rating")
            if sort_direction == "desc":
                queryset = queryset.reverse()
        # Get the category from the GET request
        category = self.request.GET.get("category")
        # Filter the queryset based on the category
        if category:
            queryset = queryset.filter(category__name=category)
        # Get the search term from the GET request
        search_term = self.request.GET.get("search", "")
        # Filter the queryset based on the search term
        if search_term:
            queryset = queryset.filter(
                Q(isbn__icontains=search_term)
                | Q(title__icontains=search_term)
                | Q(author__name__icontains=search_term)
            )
        # Get the subcategory from the GET request
        subcategory = self.request.GET.get("subcategory")

        # Filter the queryset based on the subcategory
        if subcategory:
            queryset = queryset.filter(subcategory_id=subcategory)
        # Return the filtered and ordered queryset
        return queryset

    def get_context_data(self, **kwargs):
        """Add sort order, search term, and category filter to context"""
        context = super().get_context_data(**kwargs)
        # Add the sort order, search term, and category filter to the context
        context["sort"] = self.request.GET.get("sort", "title")
        context["direction"] = self.request.GET.get("direction", "asc")
        context["search"] = self.request.GET.get("search", "")
        context["category"] = self.request.GET.get("category", "")
        # Add subcategories with books to the context
        context["subcategories"] = (
            SubCategory.objects.annotate(book_count=Count("books"))
            .filter(book_count__gt=0)
            .order_by("name")
        )
        # Add current subcategory name to the context
        subcategory = self.request.GET.get("subcategory", "")
        # Add current subcategory name to the context
        context["subcategory"] = subcategory
        if subcategory:
            current_subcategory = SubCategory.objects.get(pk=subcategory)
            context["current_subcategory_name"] = current_subcategory.name
        else:
            context["current_subcategory_name"] = None
        # Paginate the books
        paginator = Paginator(self.get_queryset(), self.paginate_by)
        page = self.request.GET.get("page")
        books = paginator.get_page(page)
        context["books"] = books

        # Add favorite books to the context
        if self.request.user.is_authenticated:
            context["favorite_books"] = set(
                FavoriteBook.objects.filter(
                    user=self.request.user
                ).values_list("book_id", flat=True)
            )
        else:
            context["favorite_books"] = set()
        return context


# The BookDetailView displays the details of a specific book


class BookDetailView(DetailView):
    """Display the details of a specific book"""

    # Specify the model to use
    model = Book
    # Specify the template name to use
    template_name = "products/book_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context["favorite_books"] = set(
                FavoriteBook.objects.filter(
                    user=self.request.user
                ).values_list("book_id", flat=True)
            )
        else:
            context["favorite_books"] = set()
        return context


# The BookCreateView allows the user to create a new book
# The user must be logged in and a staff member to access this view


class BookCreateView(CreateView):
    """Allow the user to create a new book"""

    # Specify the model to use
    model = Book
    # Specify the form to use
    form_class = BookForm
    # Specify the template name to use
    template_name = "products/book_form.html"
    # Specify the URL to redirect to after a successful submission
    success_url = reverse_lazy("products:book_list")

    # The dispatch method: Check if user is staff and logged in
    @method_decorator(
        staff_member_required(login_url=reverse_lazy("products:book_list"))
    )
    def dispatch(self, *args, **kwargs):
        """Check if the user is logged in and a staff member"""
        return super().dispatch(*args, **kwargs)

    # The form_valid method
    def form_valid(self, form):
        """Set the user field of the book to the current user"""
        book = form.save(commit=False)
        book.user = self.request.user
        book.save()
        book_title = escape(book.title)
        messages.success(
            self.request,
            f'Book "{book_title}" created successfully',
            extra_tags="created",
        )
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        """Add the action to the context"""
        context = super().get_context_data(**kwargs)
        context["action"] = "Create"
        return context


# The BookUpdateView allows the user to update a specific book
# The user must be logged in and a staff member to access this view
@method_decorator(login_required, name="dispatch")
class BookUpdateView(UpdateView):
    """Allow the user to update a specific book"""

    model = Book
    form_class = BookUpdateForm
    # Specify the template name to use
    template_name = "products/book_form.html"
    # Specify the URL to redirect to after a successful submission
    success_url = reverse_lazy("products:book_list")

    # The dispatch method: check is user staff and logged in
    @method_decorator(
        staff_member_required(login_url=reverse_lazy("products:book_list"))
    )
    def dispatch(self, *args, **kwargs):
        """Check if the user is logged in and a staff member"""
        return super().dispatch(*args, **kwargs)

    # The form_valid method
    def form_valid(self, form):
        """Set the user field of the book to the current user"""
        response = super().form_valid(form)
        book_title = escape(self.object.title)
        messages.info(
            self.request,
            f'Book "{book_title}" updated successfully',
            extra_tags="updated",
        )
        return response

    def get_context_data(self, **kwargs):
        """Add the action to the context"""
        context = super().get_context_data(**kwargs)
        context["action"] = "Update"
        return context


# The BookDeleteView allows the user to delete a specific book
# The user must be logged in and a staff member to access this view


@method_decorator(login_required, name="dispatch")
class BookDeleteView(DeleteView):
    """Allow the user to delete a specific book"""

    # Specify the model to use
    model = Book
    # Specify the template name to use
    template_name = "products/book_confirm_delete.html"

    # Redirect to the book list page on successful deletion
    success_url = reverse_lazy("products:book_list")

    # staff_member_required
    @method_decorator(staff_member_required(login_url=reverse_lazy("home")))
    def dispatch(self, request, *args, **kwargs):
        """Check if the user is logged in and a staff member"""
        return super().dispatch(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        """Display a success message after the book is deleted"""
        book = self.get_object()
        book_title = escape(book.title)
        messages.error(
            self.request,
            f'Book "{book_title}" deleted successfully',
            extra_tags="deleted",
        )
        return super().delete(request, *args, **kwargs)


# add to favorites
# The user must be logged in to access this view


@login_required
def add_to_favorites(request, book_id):
    """Add a book to the user's favorites"""
    book = get_object_or_404(Book, id=book_id)
    created = FavoriteBook.objects.get_or_create(user=request.user, book=book)

    if created:
        messages.success(
            request,
            f"'{book.title}' has been added to your favorites.",
            extra_tags="favorites",
        )
    else:
        messages.warning(
            request,
            f"'{book.title}' is already in your favorites.",
            extra_tags="favorites",
        )
    # Redirect back to the previous page
    return redirect(request.META.get("HTTP_REFERER"))


# remove from favorites
# The user must be logged in to access this view


@login_required
def remove_from_favorites(request, book_id):
    """Remove a book from the user's favorites"""
    book = get_object_or_404(Book, id=book_id)
    favorite_book = get_object_or_404(
        FavoriteBook, user=request.user, book=book
    )
    favorite_book.delete()

    messages.error(
        request,
        f"'{book.title}' has been removed from your favorites.",
        extra_tags="removed_from_favorites",
    )

    # Redirect back to the previous page
    return redirect(request.META.get("HTTP_REFERER"))
