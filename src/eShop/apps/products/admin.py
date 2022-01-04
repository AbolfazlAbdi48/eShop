from django.contrib import admin
from .models import Category, Product


# Register your models here.
class CategoryInline(admin.TabularInline):
    model = Product.categories.through


class CategoryAdmin(admin.ModelAdmin):
    list_filter = ['created', 'updated']
    search_fields = ['name']


class ProductAdmin(admin.ModelAdmin):
    inlines = [
        CategoryInline
    ]

    list_filter = ['created', 'updated', 'price']
    search_fields = ['title', 'description']
    list_display = [
        '__str__', 'thumbnail_tag', 'price_tag', 'sale_count', 'product_count', 'active', 'updated'
    ]
    list_editable = ['active']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
