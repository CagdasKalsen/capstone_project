from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Customers(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.first_name


class Category(models.Model):
    title = models.CharField(max_length=250)

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=250)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="products")
    price = models.FloatField()
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.title


class Cart(models.Model):
    customer = models.ForeignKey(
        Customers, on_delete=models.SET_NULL, null=True, blank=True)
    total = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    products = models.ManyToManyField(Product)

    def __str__(self):
        return str(self.customer.first_name) + "'s cart' "


class CartProduct(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.IntegerField()
    quantity = models.IntegerField()
    subtotal = models.IntegerField()

    def __str__(self):
        return "Cart : " + str(self.cart.id) + "CartProduct : " + str(self.id)
