from django.db import models
from .category import store_category


class store_products(models.Model):
    name = models.CharField(max_length=60)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(store_category, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=250, default='', blank=True, null=True)
    image = models.ImageField(upload_to='uploads/products/')

    @staticmethod
    def get_products_by_id(ids):
        return store_products.objects.filter(id__in=ids)

    @staticmethod
    def get_all_products():
        return store_products.objects.all()

    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return store_products.objects.filter(category=category_id)
        else:
            return store_products.get_all_products();
