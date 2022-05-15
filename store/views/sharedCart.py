from django.shortcuts import render, redirect

from ..models import store_products
from django.views import View

from ..models.sharedCart import shared_cart
from ..templatetags.cart import cart_quantity


class SharedCart(View):
    def post(self, request):
        ids = list(request.session.get('cart').keys())
        customer = request.session.get('customer')
        cart = request.session.get('cart')
        products = store_products.get_products_by_id(list(cart.keys()))
        address = request.POST.get('address')
        pincode = request.POST.get('pincode')
        phone = request.POST.get('phone')
        print(customer, cart, products, address, pincode)

        for product in products:
            print(cart.get(str(product.id)))
            order = shared_cart(shared_cart_id="SC_" + str(customer),
                                customer_id=customer,
                                image=product.image,
                                product=product.name,
                                product_id=product.id,
                                price=product.price,
                                quantity=cart_quantity(product,cart),
                                address=address,
                                pincode=pincode,
                                phone=phone)

            print("***", order)
            order.save()
        print("****")
        request.session['cart'] = {}

        return redirect('store')
