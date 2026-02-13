from django.contrib import admin
from .models import Product, OrderProduct, Customer, Cart, CartLine, Order, OrderLine, CustomProject

class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "availability")
    
class OrderProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price")

class CustomProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "customerID", "request_date")
    ordering = ("-request_date",)

admin.site.register(Product, ProductAdmin)
admin.site.register(OrderProduct, OrderProductAdmin)
admin.site.register(Customer)
admin.site.register(Cart)
admin.site.register(CartLine)
admin.site.register(Order)
admin.site.register(OrderLine)
admin.site.register(CustomProject, CustomProjectAdmin)
