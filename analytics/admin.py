from django.contrib import admin
from analytics.models.ProductViewHistory import ProductViewHistory


@admin.register(ProductViewHistory)
class ProductViewHistoryAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'created_at')
    list_select_related = ('user', 'product')
    search_fields = ('user__username', 'product__name')
    list_filter = ('created_at',)

