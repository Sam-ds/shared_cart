from django.shortcuts import render, redirect

from ..models import store_products, store_order
from ..models.customer import store_customer
from django.views import View


class CheckOut(View):
    def post(self, request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer = request.session.get('customer')
        cart = request.session.get('cart')
        products = store_products.get_products_by_id(list(cart.keys()))
        print(address, phone, customer, cart, products)

        for product in products:
            print(cart.get(str(product.id)))
            order = store_order(customer=store_customer(id=customer),
                                product=product,
                                price=product.price,
                                address=address,
                                phone=phone,
                                quantity=cart.get(str(product.id)))
            order.save()
        request.session['cart'] = {}

        return redirect('cart')
