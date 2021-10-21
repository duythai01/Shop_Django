from django.db import models

from product.models import  Product
from user.models import CustomerUser

import sys



print(sys.path)


class Cart(models.Model):
    customer_user = models.ForeignKey(CustomerUser, on_delete=models.SET_NULL, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)


class Variation(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, related_name='variations')
    price = models.IntegerField(default='')
    sale_price = models.IntegerField(default=0)
    inventory = models.IntegerField(default=0)
    active = models.BooleanField(default=True)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, related_name='product')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    quantity = models.IntegerField(default=1)
    price = models.FloatField(default=0)
    discount = models.FloatField(default=0)

    def __str__(self):
        return str(self.id)

    def get_cost(self):
        return self.price * self.quantity + ((self.price * self.quantity) * self.discount)/100

