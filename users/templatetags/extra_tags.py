from django import template
from rolepermissions.permissions import available_perm_status

register = template.Library()

def singular(value, arg):
    """Replaces all values of arg from the given string with a space"""
    if value == "repositories":
        return "repository"
    else:
        return value[:-1]

def cut(value, arg):
    """Replaces all values of arg from the given string with a space"""
    return value.replace(arg, ' ')

register.filter('singular', singular)
register.filter('cut', cut)