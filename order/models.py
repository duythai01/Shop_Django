from django.db import models

# Create your models here.
from cart.models import Cart
from user.models import CustomerUser


class Order(models.Model):
    customer_user = models.ForeignKey(CustomerUser, on_delete=models.SET_NULL, null=True)
    cart = models.ForeignKey(Cart, on_delete=models.SET_NULL, null=True)
    ship_address = models.TextField(null=True, blank=True)
    order_description = models.TextField(null=True, blank=True)
    total = models.IntegerField(default=0)
    is_completed = models.BooleanField(default = False)
