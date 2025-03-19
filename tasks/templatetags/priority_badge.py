from django import template

register = template.Library()

@register.filter
def priority_badge(priority):
    badges = {
        "urgent": "danger",
        "high": "warning",
        "medium": "success",
        "low": "info"
    }
    return badges.get(priority, "info")