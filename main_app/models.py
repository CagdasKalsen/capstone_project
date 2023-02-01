from django.db import models

# Create your models here.


class Customers(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)

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
    description = models.TextField

    def __str__(self):
        return self.title
