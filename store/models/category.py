from django.db import models


class store_category(models.Model):
    name = models.CharField(max_length=50)

    @staticmethod
    def get_all_categories():
        return store_category.objects.all()

    def __str__(self):
        return self.name
