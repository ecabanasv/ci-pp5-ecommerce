from .models import Book, Category


def book_count_processor(request):
    """A context processor that returns the count of books in the Book model"""
    # Get all categories in the Category model
    categories = Category.objects.all()

    # Create a dictionary of category counts
    category_counts = {
        category.name: Book.objects.filter(category=category).count()
        for category in categories
    }

    # Create a dictionary to store the subcategory counts for each category
    subcategory_counts = {}

    # Loop through each category
    for category in categories:
        # Get all the subcategories for the current category
        subcategories = category.subcategories.all()
        # Create a dictionary of subcategory counts for the current category
        subcategory_counts[category.name] = {
            subcategory.name: Book.objects.filter(
                subcategory=subcategory
            ).count()
            for subcategory in subcategories
        }
    # Get the count of all books in the Book model
    all_books_count = Book.objects.count()

    # Get the current category name from the GET request
    current_category_name = request.GET.get("category")

    # If the current category name exists
    if current_category_name:
        # Try to get the current category from the Category model
        try:
            current_category = Category.objects.get(name=current_category_name)
            current_category_count = Book.objects.filter(
                category=current_category
            ).count()
        # if category does not exist, set 0
        except Category.DoesNotExist:
            current_category_count = 0
    # return all_books_count
    else:
        current_category_count = all_books_count
    # Return the context
    return {
        "all_books_count": all_books_count,
        "category_counts": category_counts,
        "categories": categories,
        "subcategory_counts": subcategory_counts,
        "current_category_name": current_category_name,
        "current_category_count": current_category_count,
    }
