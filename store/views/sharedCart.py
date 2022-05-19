import string

from django.shortcuts import render, redirect
import secrets

from ..models import store_products
from django.views import View

from ..models.sharedCart import shared_cart
from ..templatetags.cart import cart_quantity
from ..models.customer import store_customer


class SharedCart(View):
    def post(self, request):
        ids = list(request.session.get('cart').keys())
        customer = request.session.get('customer')
        gcart_name = request.POST.get('gcart-name')
        print("***",gcart_name)
        cart = request.session.get('cart')
        products = store_products.get_products_by_id(list(cart.keys()))
        address = request.POST.get('address')
        pincode = request.POST.get('pincode')
        phone = request.POST.get('phone')
        customer_name = store_customer.get_customer_by_id(customer).first_name
        print(customer, cart, products, address, pincode, customer_name)
        scart_id ="SC_" + str(customer)+ "".join(
            secrets.choice(string.ascii_uppercase + string.digits) for i in range(6))
        if not gcart_name:
            for product in products:
                print(cart.get(str(product.id)))
                order = shared_cart(shared_cart_id=scart_id,
                                    customer_id=customer,
                                    image=product.image,
                                    product=product.name,
                                    product_id=product.id,
                                    price=product.price,
                                    quantity=cart_quantity(product, cart),
                                    address=address,
                                    pincode=pincode,
                                    phone=phone,
                                    ordered_by=customer_name,
                                    scart_name=scart_id)

                print("***", order)
                order.save()
        else:
            for product in products:
                print(cart.get(str(product.id)))
                order = shared_cart(shared_cart_id=scart_id,
                                    customer_id=customer,
                                    image=product.image,
                                    product=product.name,
                                    product_id=product.id,
                                    price=product.price,
                                    quantity=cart_quantity(product, cart),
                                    address=address,
                                    pincode=pincode,
                                    phone=phone,
                                    ordered_by=customer_name,
                                    scart_name=gcart_name)

                print("***", order)
                order.save()

        print("****")
        request.session['cart'] = {}

        return redirect('gcart')
