from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from store.models.product import Product
from store.models.category import Category
from django.views import View
from django.views.decorators.http import require_http_methods


class CheckOut(View) :
    def post(self, request) :
        product = request.POST.get('product')
        customer=request.POST.get('customer')
        quantity=request.POST.get('quantity')
        price=request.POST.get('price')
        customer = request.session.get('customer')
        cart = request.session.get('cart')
        products = Product.get_products_by_id(list(cart.keys()))
        print(quantity,customer,cart,products)

        for product in products:
            order = Order(customer=Customer(id = customer),product = product,
                          price = product.price,quantity = cart.get(str(product.id)))
            order.save()
        request.session['cart']={}
        return redirect('cart')