from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Banner(models.Model):
    title = models.CharField(max_length = 150)
    image = models.ImageField(upload_to='BannerImage')
    http_link = models.URLField(max_length = 300, blank=True, null=True)

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length = 150)
    parent_category  = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='child')
    image = models.ImageField(upload_to='CategoryImage')

    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length = 150)
    image = models.ImageField(upload_to='BrandImage')

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length = 150)
    image = models.ImageField(upload_to='ProductImage')
    price  = models.IntegerField()
    discount_price = models.IntegerField(blank=True, null=True)
    description  = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    quantity  = models.IntegerField()

    def __str__(self):
        return self.name

class CartProduct(models.Model):
    user  = models.ForeignKey(User, on_delete=models.CASCADE)
    product  = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.product.name

class Order(models.Model):
    user  = models.ForeignKey(User, on_delete=models.CASCADE)
    cart_products = models.ManyToManyField(CartProduct)
    ordered = models.BooleanField(default=False)
    ordered_date = models.DateTimeField()
    
    def __str__(self):
        return self.user
    
    
    
    
    

class ProductImages():
    pass
    
    

    
    
    
