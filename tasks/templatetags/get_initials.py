from django import template

register = template.Library()


@register.filter
def get_initials(worker):
    if worker.first_name and worker.last_name:
        return f"{worker.first_name[0]}{worker.last_name[0]}".upper()
    return worker.username[:2].upper()
