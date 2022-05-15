from django.shortcuts import render, redirect
from django.views import View
from ..models.orders import store_order


class OrderView(View):

    def get(self, request):
        customer = request.session.get('customer')
        orders = store_order.get_orders_by_customer(customer)
        print(orders)
        return render(request, 'orders.html', {'orders': orders})
