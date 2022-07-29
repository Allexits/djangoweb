from django.urls import path
from django.contrib import admin
from .views import *


urlpatterns = [
    path('', index, name ='home'),
    path('about', about, name ='about'),
    path('shops', shop, name ='shops'),
    path('shop/<slug:page_slug>/', shop, name ='shop'),
    path('cart', cart, name ='cart')
]