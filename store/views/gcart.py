from django.shortcuts import render, redirect

from django.views import View
from ..models.sharedCart import shared_cart


class gcart(View):
    def get(self, request):
        shared_cart_available=""
        customer = request.session.get('customer')
        shared_cart_items = shared_cart.get_orders_by_customer(customer)
        print(shared_cart_items)
        shared_cart_items_total = shared_cart.get_total_price(customer)
        print(shared_cart_items_total)
        shared_cart_ids = set()
        shared_cart_items_dict = {}
        if len(shared_cart_items) > 0:
            id_count = 0
            for cart in shared_cart_items:
                shared_cart_ids.add(cart.shared_cart_id)
                id_count = id_count + 1
            sid_count = 0
            for ids in shared_cart_ids:
                shared_cart_items_dict[ids] = shared_cart.get_orders_by_cartid(ids)
                sid_count = sid_count + 1

        else:
            shared_cart_ids = ()
        print(shared_cart_ids)
        if len(shared_cart_ids) == 0:
            shared_cart_available = "empty"
        print( "@@@",shared_cart_items_dict)
        return render(request, 'gcart.html', {
            'shared_cart_items_dict': shared_cart_items_dict,
            'shared_cart_items_total': shared_cart_items_total.get('result'),
            'shared_cart_id': shared_cart_ids,
            'shared_cart_available': shared_cart_available})
