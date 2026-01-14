from django.contrib import admin
from django.utils.html import format_html

from .models import Product, ProductImage


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'category', 'price', 'stock', 'owner', 'created_at', 'updated_at')
    search_fields = ('name', )
    list_filter = ('category', 'price')


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'is_main', 'preview')
    list_editable = ('is_main',)
    readonly_fields = ('preview',)

    def preview(self, obj):
        return format_html('<img src="{}" width="40"/>', obj.image.url) if obj.image else '-'

