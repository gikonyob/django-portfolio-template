from django import template
from rolepermissions.permissions import available_perm_status

register = template.Library()

def cut(value, arg):
    """Replaces all values of arg from the given string with a space"""
    return value[:-1]

register.filter('cut', cut)