# from django.contrib import admin
# from django.utils.html import format_html
# from .models import FlashSale, FlashSaleNotification, ProductViewHistory
#
#
# @admin.register(FlashSale)
# class FlashSaleAdmin(admin.ModelAdmin):
#     list_display = [
#         'product',
#         'discount_percentage',
#         'status_badge',
#         'sale_price',
#         'remaining_stock',
#         'start_time',
#         'end_time',
#         'is_active'
#     ]
#     list_filter = ['status', 'is_active', 'start_time']
#     search_fields = ['product__name']
#     readonly_fields = ['sale_price', 'sold_quantity', 'status']
#     date_hierarchy = 'start_time'
#
#     fieldsets = (
#         ('Asosiy ma\'lumotlar', {
#             'fields': ('product', 'discount_percentage', 'original_price', 'sale_price')
#         }),
#         ('Miqdor', {
#             'fields': ('quantity', 'sold_quantity')
#         }),
#         ('Vaqt', {
#             'fields': ('start_time', 'end_time')
#         }),
#         ('Status', {
#             'fields': ('is_active', 'status')
#         }),
#     )
#
#     def status_badge(self, obj):
#         colors = {
#             'scheduled': 'blue',
#             'active': 'green',
#             'expired': 'red',
#             'cancelled': 'gray',
#         }
#         color = colors.get(obj.status, 'gray')
#         return format_html(
#             '<span style="background-color: {}; color: white; padding: 3px 10px; border-radius: 3px;">{}</span>',
#             color,
#             obj.get_status_display()
#         )
#
#     status_badge.short_description = 'Status'
#
#     def remaining_stock(self, obj):
#         return f"{obj.remaining_quantity()} / {obj.quantity}"
#
#     remaining_stock.short_description = 'Qolgan / Jami'
#
#
# @admin.register(FlashSaleNotification)
# class FlashSaleNotificationAdmin(admin.ModelAdmin):
#     list_display = ['user', 'flash_sale', 'is_sent', 'sent_at', 'created_at']
#     list_filter = ['is_sent', 'created_at']
#     search_fields = ['user__username', 'flash_sale__product__name']
#
#
# @admin.register(ProductViewHistory)
# class ProductViewHistoryAdmin(admin.ModelAdmin):
#     list_display = ['user', 'product', 'view_count', 'last_viewed']
#     list_filter = ['last_viewed']
#     search_fields = ['user__username', 'product__name']