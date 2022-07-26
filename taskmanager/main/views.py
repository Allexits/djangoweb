from django.shortcuts import render



def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def shop(request):
    return render(request, 'main/shop.html')

def shop_id(request,id):
    return render(request, 'main/shop_id.html')


def cart(request):
    return render(request, 'main/cart.html')