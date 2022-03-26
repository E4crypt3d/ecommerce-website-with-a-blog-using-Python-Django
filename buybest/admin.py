from django.contrib import admin
from .models import Contact, Order, Product, UpdateOrder
# Register your models here.
admin.site.register(Product)
admin.site.register(Contact)
admin.site.register(Order)
admin.site.register(UpdateOrder)