from django.db import models
from products.models import Product
# Create your models here.

class Item(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    total = models.FloatField( default=0.00)