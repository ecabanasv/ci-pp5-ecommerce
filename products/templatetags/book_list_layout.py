from django import template

register = template.Library()


# The col_value function returns the number of columns to be used for a specific number of books

@register.filter
def col_value(total_books):
    if total_books == 1:
        return 4
    elif total_books == 2:
        return 4
    elif total_books == 3:
        return 4
    elif total_books <= 5:
        return 5
    else:
        return 4

# The col_lg_value function returns the number of columns to be used for a specific number of books

@register.filter
def col_lg_value(total_books):
    if total_books == 1:
        return 6
    elif total_books == 2:
        return 6
    elif total_books == 3:
        return 6
    elif total_books <= 5:
        return 6
    else:
        return 6

# The row_value function returns the number of rows to be used for a specific number of books

@register.filter
def row_value(total_books):
    if total_books <= 3:
        return 1
    elif total_books <= 6:
        return 2
    else:
        return 3

# The items_per_row function returns the number of books to be displayed per row

@register.filter
def items_per_row(total_books):
    return total_books // row_value(total_books)
