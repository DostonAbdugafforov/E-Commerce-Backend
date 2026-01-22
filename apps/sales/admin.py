from django.contrib import admin
from apps.sales.models.FlashSale import FlashSale
from apps.sales.models.FlashSaleNotification import FlashSaleNotification

@admin.register(FlashSale)
class FlashSaleAdmin(admin.ModelAdmin):
    list_display = [
        'product',
        'discount_percentage',
        'sale_price',
        'quantity',
        'sold_quantity',
        'remaining_stock',
        'start_time',
        'end_time',
        'is_active',
        'status',
    ]
    list_filter = ['status', 'is_active', 'start_time']
    search_fields = ['product__name']
    readonly_fields = ['sale_price', 'sold_quantity', 'status']
    date_hierarchy = 'start_time'

    def remaining_stock(self, obj):
        return f"{obj.remaining_quantity()} / {obj.quantity}"

    remaining_stock.short_description = 'Qolgan / Jami'


@admin.register(FlashSaleNotification)
class FlashSaleNotificationAdmin(admin.ModelAdmin):
    list_display = ['user', 'flash_sale', 'is_read', 'created_at', 'updated_at']
    list_filter = ['created_at', ]
    search_fields = ['user__username', 'flash_sale__product__name']
