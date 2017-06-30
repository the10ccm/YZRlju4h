from django import template
from datetime import date

register = template.Library()

@register.simple_tag
def is_allowed_by_birthday(birthday):
    """ Returns 'allowed' if the birthday is greater than 13 years """
    diff = date.today().year - birthday.year
    return 'allowed' if diff else 'blocked'

@register.simple_tag
def bizzfuzz(number):
    """ Return transformed BizzFuzz string according to:
        number % 3 -> 'Bizz',
        number % 5 -> 'Fuzz'
        number % 3 and number % 5 -> 'BizzFuzz'
        any -> origin
    """
    if not number % 3 and not number % 5:
        return 'BizzFuzz'
    elif not number % 5:
        return 'Fuzz'
    elif not number % 3:
        return 'Bizz'
    return number
