from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name ='home'),
    path('about', about, name ='about'),
    path('shops', shop, name ='shops'),
    path('shop/<int:id>/', shop, name ='shop'),
    path('cart', cart, name ='cart'),
    path('login', login, name ='login')
]