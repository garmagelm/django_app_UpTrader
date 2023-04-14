from django import template
from menu_app.models import MenuItem

register = template.Library()

@register.inclusion_tag('menu_app/menu.html')
def draw_menu(menu_name):
    menu_items = MenuItem.objects.filter(menu_name=menu_name, parent=None)
    return {'menu_items': menu_items}
