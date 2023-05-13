from django.contrib import admin
from .models import PizzaMenu,OrderModel

# Register your models here.
admin.site.register(PizzaMenu)
admin.site.register(OrderModel)