from django.contrib import admin
from .models import Order 


# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    list_display = ['barber', 'customer', 'time']

admin.site.register(Order, OrderAdmin)
