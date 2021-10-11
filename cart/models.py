from django.db import models

from product.models import Variation
from user.models import CustomerUser


class Cart(models.Model):
    customer_user = models.ForeignKey(CustomerUser, on_delete=models.SET_NULL, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.SET_NULL, null=True)
    item = models.ForeignKey(Variation, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0)
