from django.shortcuts import render,redirect,get_object_or_404

from .models import *
from django.core import serializers


def index(request):
    page = Menu.objects.get(slug='home')
    context = {
        'page':page
        }
    return render(request, 'main/index.html',context = context)


def about(request):
    page = Menu.objects.get(slug='about')
    context = {
        'page':page
        }
    return render(request, 'main/about.html',context = context)

def shop(request,page_slug=''):
    page = Menu.objects.get(slug='shops')
    if page_slug=='':
        cur_shop = Shops.objects.order_by('pk').first()
    else:
        cur_shop = get_object_or_404(Shops,slug=page_slug)
    products = Products.objects.filter(category=cur_shop.pk,is_active=1)
    context = {
        'page':page,
        'cur_shop':cur_shop,
        'products':products,
        'shop_sel':cur_shop.pk
    }
    return render(request, 'main/shop.html',context = context)


def cart(request):
    page = Menu.objects.get(slug='cart')
    data = serializers.serialize("json", Products.objects.all())
    context = {
        'page':page,
        'data':data
        }
    return render(request, 'main/cart.html',context = context)

