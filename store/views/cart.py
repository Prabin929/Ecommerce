from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from store.models.product import Product
from store.models.category import Category
from django.views import View
from django.views.decorators.http import require_http_methods


class Cart(View) :
    def post(self, request) :
        return None

    def get(self, request) :
        ids = list(request.session.get('cart').keys())
        products = Product.get_products_by_id(ids)
        print(products)
        return render(request, 'cart.html',{'products':products})
