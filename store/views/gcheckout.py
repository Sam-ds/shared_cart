from django.shortcuts import render, redirect

from ..models import store_products, store_order
from ..models.customer import store_customer
from django.views import View
from ..models.sharedCart import shared_cart


class gcheckout(View):

    def post(self, request):
        shared_cart_items = shared_cart.get_orders_by_cartid(request.POST.get('group_cart_id'))
        for details in shared_cart_items:
            details.checkout_done=1
            details.save()

        return redirect('cart')
