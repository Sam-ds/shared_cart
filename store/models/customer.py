from django.db import models


class store_customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    password = models.CharField(max_length=100)

    # to save the data
    def register(self):
        self.save()

    @staticmethod
    def get_customer_by_email(email):
        try:
            return store_customer.objects.get(email=email)
        except:
            return False

    @staticmethod
    def get_customer_by_id(id):
        try:
            return store_customer.objects.get(id=id)
        except:
            return False

    def isExists(self):
        if store_customer.objects.filter(email=self.email):
            return True

        return False
