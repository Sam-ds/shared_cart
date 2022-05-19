from django.shortcuts import render, redirect
from django.template import context

from django.views import View
from ..models.product import store_products
from ..models.sharedCart import shared_cart


class SCheckout(View):
    def get(self, request):
        customer = request.session.get('customer')
        shared_cart_items = shared_cart.get_orders_by_customer(customer)
        print(shared_cart_items)
        products = shared_cart.get_orders_by_cartid(request.GET.get('shared_cart_id'))
        for product in products:
            print(product.product_id)

        print("***")
        print(request.GET.get('shared_cart_id'))
        print(products)
        shared_cart_items_total = shared_cart.get_total_price(customer)
        print(shared_cart_items_total)
        if len(shared_cart_items) > 0:
            shared_cart_id = shared_cart_items[0].shared_cart_id
        else:
            shared_cart_id = "empty"
        print(shared_cart_id)
        return render(request, 'gcart.html', {
            'shared_cart_items': shared_cart_items,
            'shared_cart_items_total': shared_cart_items_total.get('result'),
            'shared_cart_id': shared_cart_id})
