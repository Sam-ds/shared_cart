from django.db import models
from django.db.models import Sum,F

from .product import store_products


class shared_cart(models.Model):
    shared_cart_id = models.CharField(max_length=50)
    product = models.CharField(max_length=50)
    image = models.CharField(max_length=100)
    customer_id = models.IntegerField()
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    address = models.CharField(max_length=50, default='', blank=True)
    phone = models.CharField(max_length=50, default='', blank=True)
    pincode = models.CharField(max_length=10, default='', blank=True)
    product_id=models.IntegerField()

    def placeOrderShared(self):
        self.save()

    @staticmethod
    def get_orders_by_customer(customer_id):
        return shared_cart.objects.filter(customer_id=customer_id)

    @staticmethod
    def get_orders_by_cartid(shared_cart_id):
        return shared_cart.objects.filter(shared_cart_id=shared_cart_id)

    @staticmethod
    def get_total_price(customer_id):
        return shared_cart.get_orders_by_customer(customer_id).aggregate(result = Sum(F("price") * F("quantity")))
