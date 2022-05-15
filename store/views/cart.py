from django.shortcuts import render, redirect

from django.views import View
from ..models.product import store_products
from ..models.sharedCart import shared_cart


class Cart(View):
    def get(self, request):
        cart=request.session.get('cart')
        products = shared_cart.get_orders_by_cartid(request.GET.get('shared_cart_id'))
        for product in products:
            print(product.product_id)
            cart.update({product.product_id:product.quantity})
        request.session['cart'] = cart

        ids = list(request.session.get('cart').keys())
        customer = request.session.get('customer')
        shared_cart_items = shared_cart.get_orders_by_customer(customer)
        print(shared_cart_items)
        products = store_products.get_products_by_id(ids)
        print(products)
        shared_cart_items_total = shared_cart.get_total_price(customer)
        print(shared_cart_items_total)
        if len(shared_cart_items) > 0:
            shared_cart_id = shared_cart_items[0].shared_cart_id
        else:
            shared_cart_id= "empty"
        print(shared_cart_id)
        return render(request, 'cart.html', {'products': products,
                                             'shared_cart_items': shared_cart_items,
                                             'shared_cart_items_total': shared_cart_items_total.get('result'),
                                             'shared_cart_id': shared_cart_id})
