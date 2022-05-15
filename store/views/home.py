from django.shortcuts import render, redirect, HttpResponseRedirect

from django.views import View


# Create your views here.
from ..models import store_category, store_products


class Index(View):

    def post(self, request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity <= 1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity - 1
                else:
                    cart[product] = quantity + 1

            else:
                cart[product] = 1
        else:
            cart = {product: 1}

        request.session['cart'] = cart
        print('cart', request.session['cart'])
        return redirect('homepage')

    def get(self, request):
        # print()
        return HttpResponseRedirect(f'/store{request.get_full_path()[1:]}')


def store(request):
    cart = request.session.get('cart')
    if not cart:
        request.session['cart'] = {}
    products = None
    categories = store_category.get_all_categories()
    categoryID = request.GET.get('category')
    if categoryID:
        products = store_products.get_all_products_by_categoryid(categoryID)
    else:
        products = store_products.get_all_products();

    data = {'products': products, 'categories': categories}

    print('you are : ', request.session.get('email'))
    return render(request, 'index.html', data)
