from django.urls import path
from .views import (
    BookListView,
    BookDetailView,
    BookCreateView,
    BookUpdateView,
    BookDeleteView,
    search_books,
    add_to_favorites,
    remove_from_favorites,
)

app_name = "products"

urlpatterns = [
    # List all books
    path("", BookListView.as_view(), name="book_list"),
    # Detail view for a specific book
    path("<int:pk>/", BookDetailView.as_view(), name="book_detail"),
    # Create a new book
    path("new/", BookCreateView.as_view(), name="book_create"),
    # Update an existing book
    path("<int:pk>/update/", BookUpdateView.as_view(), name="book_update"),
    # Delete an existing book
    path("<int:pk>/delete/", BookDeleteView.as_view(), name="book_delete"),
    # Search for books
    path("search/", search_books, name="book_search"),
    # Add to favourites
    path(
        "add_to_favorites/<int:book_id>/",
        add_to_favorites,
        name="add_to_favorites",
    ),
    # Remove from favourites
    path(
        "remove_from_favorites/<int:book_id>/",
        remove_from_favorites,
        name="remove_from_favorites",
    ),
]
