from django.shortcuts import render, redirect
from django.views import View
from ..models.orders import store_order
from ..models.sharedCart import shared_cart


class OrderView(View):

    def get(self, request):
        customer = request.session.get('customer')
        orders = store_order.get_orders_by_customer(customer)
        print(orders)
        shared_cart_items = shared_cart.get_orders_by_checkout_done(customer, 1)
        print(shared_cart_items)

        return render(request, 'orders.html', {'orders': orders,"shared_cart_items":shared_cart_items})
