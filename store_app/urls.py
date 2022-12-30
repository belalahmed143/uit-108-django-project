from django.urls import path 
from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('product/detail/<pk>', product_detail, name='product-detail'),
    path('search/', product_search, name='search'),
    path('about', about, name='about'),
    path('category/product/<pk>',category_filtering, name='category-filter'),
    path('add-to-cart/<pk>',add_to_cart, name='add_to_cart'),
    path('add-inc/<pk>',inc_cart, name='inc-cart'),
    path('add-dec/<pk>',dec_cart, name='dec-cart'),
    path('cart_remove/<pk>',cart_remove, name='cart_remove'),
    path('cart-summary',cart_summary, name='cart-summary'),

]