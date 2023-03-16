from django import template

register = template.Library()

@register.filter
def col_value(total_books):
    if total_books == 1:
        return 12
    elif total_books == 2:
        return 6
    elif total_books == 3:
        return 4
    elif total_books <= 5:
        return 6
    else:
        return 4

@register.filter
def col_lg_value(total_books):
    if total_books == 1:
        return 12
    elif total_books == 2:
        return 6
    elif total_books == 3:
        return 6
    elif total_books <= 5:
        return 6
    else:
        return 6


@register.filter
def row_value(total_books):
    if total_books <= 3:
        return 1
    elif total_books <= 6:
        return 2
    else:
        return 3

@register.filter
def items_per_row(total_books):
    return total_books // row_value(total_books)
