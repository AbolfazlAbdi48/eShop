from django.contrib import admin
from .models import Customer


# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    def has_change_permission(self, request, obj=None):
        return False

    list_filter = ['created', 'updated']
    search_fields = ['email']


admin.site.register(Customer, CustomerAdmin)
