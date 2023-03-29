from .models import Book, Category


def book_count_processor(request):
    # Get all categories in the Category model
    categories = Category.objects.all()

    # Create a dictionary where the keys are the category names, and the values are the count of books in each category
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
        # Create a dictionary where the keys are the subcategory names, and the values are the count of books in each subcategory
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

    # If there is a current category name, try to get the Category object with that name
    if current_category_name:
        try:
            current_category = Category.objects.get(name=current_category_name)
            current_category_count = Book.objects.filter(
                category=current_category
            ).count()
        # If the Category object with the current category name doesn't exist, set the current category count to 0
        except Category.DoesNotExist:
            current_category_count = 0
    # If there isn't a current category name, set the current category count to the count of all books
    else:
        current_category_count = all_books_count
    # Return the all_books_count, category_counts, categories, subcategory_counts, current_category_name, and current_category_count as context variables
    return {
        "all_books_count": all_books_count,
        "category_counts": category_counts,
        "categories": categories,
        "subcategory_counts": subcategory_counts,
        "current_category_name": current_category_name,
        "current_category_count": current_category_count,
    }
