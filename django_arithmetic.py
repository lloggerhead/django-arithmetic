from django import template

"""It's sometimes really handy to be able to do basic arithmetic in
Django templates.

"""

# todo: add multiple, divide, exponent, quotient
# todo: unit tests
# todo: handle None gracefully
# todo: investigate naming these +, - etc so {{ x|+:2 }} works


register = template.Library()


@register.filter
def subtract(value, arg):
    return value - arg


@register.filter
def add(value, arg):
    return value + arg
