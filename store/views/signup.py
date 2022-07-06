from django.shortcuts import render,redirect
from django.contrib.auth.hashers import make_password
from store.models.customer import Customer
from django.views import View
from django.views.decorators.http import require_http_methods


class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        fullname = request.POST.get('fullname')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        password = request.POST.get('password')
        # validation
        value = {
            'fullname' : fullname,
            'address' : address,
            'phone' : phone,
            'email' : email
        }
        error_message = None
        customer = Customer(fullname=fullname, address=address, phone=phone,
                            email=email, password=password)
        error_message = self.validateCustomer(customer)

        # saving
        if not error_message :

            customer.password = make_password(customer.password)
            customer.register()

        else :
            data = {
                'error' : error_message,
                'values' : value
            }
            return render(request, 'signup.html', data)
        return redirect('home')

    def validateCustomer(self,customer) :
        error_message = None
        if (not customer.fullname) :
            error_message = 'Fullname Required !!'
        elif len(customer.fullname) < 4 :
            error_message = 'Full name must be 6 char'
        elif customer.isExists() :
            error_message = 'Email Already Exist..'
        return error_message