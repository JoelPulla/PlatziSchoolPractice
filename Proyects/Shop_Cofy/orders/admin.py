from django.contrib import admin
from orders.models import Order, OrderProduct

# Register your models here.

#inlines
class OrderProductInLineAdmin(admin.TabularInline):
    model= OrderProduct
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    model = Order
    inlines = [
        OrderProductInLineAdmin
    ]
admin.site.register(Order, OrderAdmin)