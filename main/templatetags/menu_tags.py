from django import template
from main.menu_items import get_menu_items

register = template.Library()

@register.simple_tag
def get_menu():
    return get_menu_items()
