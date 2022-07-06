from django.db import models
from django.views.decorators.http import require_http_methods

class Customer(models.Model):
    fullname = models.CharField(max_length = 50)
    address = models.CharField(max_length = 50)
    phone = models.IntegerField()
    email = models.EmailField(unique = True)
    password = models.CharField(max_length=15)

    def register(self):
        self.save()

    @staticmethod
    def get_customer_by_email(email) :
        try:
            return Customer.objects.get(email=email)
        except:
            return False


    def isExists(self):
        if Customer.objects.filter(email = self.email):
            return True

        return False



