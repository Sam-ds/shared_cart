from django.db import models
from .product import store_products
from .customer import store_customer
import datetime


class store_order(models.Model):
    product = models.ForeignKey(store_products,
                                on_delete=models.CASCADE)
    customer = models.ForeignKey(store_customer,
                                 on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    address = models.CharField (max_length=50, default='', blank=True)
    phone = models.CharField (max_length=50, default='', blank=True)
    date = models.DateField (default=datetime.datetime.today)
    status = models.BooleanField (default=False)

    def placeOrder(self):
        self.save()

    @staticmethod
    def get_orders_by_customer(customer_id):
        return store_order.objects.filter(customer=customer_id).order_by('-date')

