from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name ='home'),
    path('about', about, name ='about'),
    path('shop', shop, name ='shop'),
    path('shop/<int:id>/', shop_id, name ='shop'),
    path('cart', cart, name ='cart')
]