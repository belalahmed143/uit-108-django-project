from django.urls import path 
from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('product/detail/<pk>', product_detail, name='product-detail'),
    path('search/', product_search, name='search'),
    path('about', about, name='about'),
    path('category/product/<pk>',category_filtering, name='category-filter'),
    path('add-to-cart/<pk>',add_to_cart, name='add_to_cart'),
]