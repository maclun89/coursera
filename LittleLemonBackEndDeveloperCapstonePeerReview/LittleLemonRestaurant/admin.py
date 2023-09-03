from django.contrib import admin
from LittleLemonDRF.models import Booking, Category, MenuItem, Cart, Order, OrderItem


# Register your models here.
admin.site.register([Booking, MenuItem])
admin.site.register(Category)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(OrderItem)

