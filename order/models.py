from django.db import models

# Create your models here.
from cart.models import Cart, CartItem
from user.models import CustomerUser


class Order(models.Model):
    customer_user = models.ForeignKey(CustomerUser, on_delete=models.SET_NULL, null=True)
    cart_item = models.ForeignKey(CartItem, on_delete=models.SET_NULL, null=True, related_name='items')
    ship_address = models.TextField(null=True, blank=True)
    order_description = models.TextField(null=True, blank=True)
    total = models.IntegerField(default=0)
    is_completed = models.BooleanField(default=False)

    def get_total_price(self):
        total = sum(item.get_cost() for item in self.items.all())

