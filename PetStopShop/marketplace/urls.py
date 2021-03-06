from django.urls import path
from .views import *

urlpatterns=[
    path('', marketplace, name='marketplace'),
    path('product/<int:id>', product, name='marketplace-product'),
    path('cart/<int:id>', update_cart, name='update_cart'),
    path('search', search_marketplace, name='search-marketplace'),
    path('cart', viewCart, name='cart'),
    path('checkout', checkout, name='checkout'),
    path('user_add_address/', user_add_address, name='user_add_address'),

]
