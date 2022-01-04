from django.contrib import admin
from .models import Payment, Address, Order, OrderDetail


# Register your models here.
class OrderDetailInline(admin.TabularInline):
    model = OrderDetail


class PaymentAdmin(admin.ModelAdmin):
    def has_change_permission(self, request, obj=None):
        return False

    list_display = ['__str__', 'amount', 'get_status', 'trace_number', 'insert_date_time', 'payment_date_time']
    list_filter = ['status', 'insert_date_time', 'payment_date_time']
    search_fields = ['amount']


class AddressAdmin(admin.ModelAdmin):
    def has_change_permission(self, request, obj=None):
        return False

    list_display = ['city', 'code_postal', 'owner', 'phone_number']
    list_filter = ['city']
    search_fields = ['full_address']


class OrderAdmin(admin.ModelAdmin):
    def has_change_permission(self, request, obj=None):
        return False

    inlines = [
        OrderDetailInline
    ]

    list_display = ['__str__', 'is_sent', 'created']
    list_filter = ['is_sent']


class OrderDetailAdmin(admin.ModelAdmin):
    def has_change_permission(self, request, obj=None):
        return False

    list_display = ['__str__', 'product', 'price', 'count', 'get_sum_price']
    list_filter = ['created']


admin.site.register(Payment, PaymentAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderDetail, OrderDetailAdmin)
