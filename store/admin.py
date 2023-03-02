from django.contrib import admin

# Register your models here.
from .models.product import Products
from .models.category import Category
from .models.customer import Customer
from .models.orders import Order
from .models.payment import Payment
from store.models.mail import userotp


class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

# Register your models here.
admin.site.register(Products,AdminProduct)
admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Payment)
admin.site.register(userotp)


# username = admin, email = admin@gmail.com, password = 1234
