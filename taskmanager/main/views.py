from django.shortcuts import render,redirect

from .models import *

shops = Shops.objects.all().order_by('id')
menu = [{'title':'Main','url_name':'home'},
        {'title':'Shops','url_name':'shops'},
        {'title':'Shoping cart','url_name':'cart'},
        {'title':'About us','url_name':'about'},
        {'title':'Login','url_name':'login'}]


def index(request):
    
    context = {
        'title':'Main',
        'shops':shops,
        'menu':menu
        }
    return render(request, 'main/index.html',context = context)


def about(request):
    context = {
        'title':'About',
        'menu':menu
    }
    return render(request, 'main/about.html',context = context)

def shop(request,id=1):
    cur_shop = Shops.objects.filter(pk=id)
    products = Products.objects.filter(category=id)
    context = {
        'title':'Shops',
        'shops':shops,
        'cur_shop':cur_shop,
        'products':products,
        'menu':menu
    }
    return render(request, 'main/shop.html',context = context)


def cart(request):
    context = {
        'title':'Shoping Cart',
        'menu':menu
    }
    return render(request, 'main/cart.html',context = context)


def login(request):
    return redirect('admin')