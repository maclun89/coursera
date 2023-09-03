from django.contrib import admin
from .models import Booking, Category, MenuItem, Cart, Order, OrderItem


# Register your models here.
admin.site.register([Booking, MenuItem, Category, Cart, Order, OrderItem])

