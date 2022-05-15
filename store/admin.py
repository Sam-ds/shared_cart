from django.contrib import admin
from .models.product import store_products
from .models.category import store_category
from .models.customer import store_customer
from .models.orders import store_order


class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


# Register your models here.
admin.site.register(store_products, AdminProduct)
admin.site.register(store_category)
admin.site.register(store_customer)
admin.site.register(store_order)

