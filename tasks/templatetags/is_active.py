from django import template

register = template.Library()


@register.filter
def is_active(url_name, valid_names):
    return url_name in valid_names
