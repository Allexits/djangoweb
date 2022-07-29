from atexit import register
from django import template
from main.models import *

register = template.Library()
 

@register.simple_tag()
def get_shops():
    return Shops.objects.filter(is_active=1).order_by('pk')
     
@register.inclusion_tag('main/menu_shop.html')
def show_shops(shop_sel=1):
    shops = Shops.objects.filter(is_active=1).order_by('pk')
    return {'shops':shops,'shop_sel':shop_sel}

@register.inclusion_tag('main/menu.html')
def show_menu():
    menu = Menu.objects.filter(is_active=1).order_by('pk')
    return {'menu':menu}      