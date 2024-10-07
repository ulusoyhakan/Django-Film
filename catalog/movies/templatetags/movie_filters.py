from django import template

register = template.Library()

@register.filter(name='truncate')
def truncate(value, max_length=200):
    """
    Cuts off the string at 'max_length' characters and appends '...' if it's longer.
    """
    if len(value) > max_length:
        return value[:max_length] + '...'
    return value
