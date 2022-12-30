from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.db.models import Q
from django.contrib import messages
from django.utils import timezone
# Create your views here.

def home(request):
    banner = Banner.objects.all()
    categories = Category.objects.all()
    brands = Brand.objects.all()
    products = Product.objects.all()
    context ={
        'banner':banner,
        'categories':categories,
        'brands':brands,
        'products':products
    }
    return render(request, 'store/index.html', context)

def product_detail(request,pk):
    product = Product.objects.get(pk=pk)
    related_product = Product.objects.filter(Q(category=product.category) | Q(brand=product.brand)).exclude(pk=pk)

    context = {
        'product':product,
        'related_product':related_product
    }
    return render(request, 'store/product-detail.html', context)

from django.core.paginator import Paginator


def product_search(request):
    query = request.GET['q']
    lookup = Q(name__icontains=query) | Q(price__icontains=query) | Q(discount_price__icontains=query) | Q(brand__name__icontains=query)
    products = Product.objects.filter(lookup)

    context = {
        'products':products,
        
    }
    return render(request, 'store/product-search.html', context)

def category_filtering(request,pk):
    cate = get_object_or_404(Category,pk=pk)
    products = Product.objects.filter(category=cate.id)

    paginator = Paginator(products, 1 ) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context={
        'page_obj':page_obj
    }
    return render(request, 'store/category.html',context)


def about(request):
    return render(request, 'store/about.html')


def add_to_cart(request,pk):
    product = get_object_or_404(Product,pk=pk)
    cartproduct , created = CartProduct.objects.get_or_create(product=product, user=request.user, ordered=False)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.cart_products.filter(product__id=product.id).exists():
            cartproduct.quantity += 1
            cartproduct.save()
            messages.info(request, 'quantity updated')
            return redirect('product-detail', pk=pk)
        else:
            order.cart_products.add(cartproduct)
            messages.info(request, 'this product add to cart')
            return redirect('product-detail', pk=pk)
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(user=request.user,ordered_date=ordered_date)
        order.cart_products.add(cartproduct)
        messages.info(request, 'this product add to cart')
        return redirect('product-detail', pk=pk)
    return redirect('product-detail', pk=pk)


def inc_cart(request,pk):
    product = get_object_or_404(Product,pk=pk)
    cartproduct , created = CartProduct.objects.get_or_create(product=product, user=request.user, ordered=False)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.cart_products.filter(product__id=product.id).exists():
            cartproduct.quantity += 1
            cartproduct.save()
            messages.info(request, 'quantity updated')
            return redirect('cart-summary')

    else:
        return redirect('cart-summary')
    return redirect('cart-summary')

def dec_cart(request,pk):
    product = get_object_or_404(Product,pk=pk)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.cart_products.filter(product__id=product.id).exists():
            cartproduct = CartProduct.objects.filter(product=product, user=request.user, ordered=False)[0]
            if cartproduct.quantity > 1:
                cartproduct.quantity -= 1
                cartproduct.save()
                messages.info(request, 'quantity updated')
                return redirect('cart-summary')
            else:
                cartproduct.delete()
                messages.info(request, 'cart-item delete')
                return redirect('cart-summary')
    else:
        return redirect('cart-summary')
    return redirect('cart-summary')

def cart_remove(request,pk):
    product = get_object_or_404(Product,pk=pk)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.cart_products.filter(product__id=product.id).exists():
            cartproduct = CartProduct.objects.filter(product=product, user=request.user, ordered=False)[0]
            cartproduct.delete()
            messages.warning(request, 'quantity updated')
            return redirect('cart-summary')
        else:
            messages.warning(request, 'this product already delete')
            return redirect('cart-summary')
    else:
        messages.warning(request, 'this product already delete')
        return redirect('cart-summary')
    return redirect('cart-summary')


def cart_summary(request):
    order = Order.objects.get(user=request.user, ordered=False)

    context={
       'order':order
    }
    return render(request, 'store/cart-summary.html', context)
