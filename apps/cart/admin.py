from django.contrib import admin
from apps.cart.models.Cart import Cart
from apps.cart.models.CartItem import CartItem


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'status',
        'created_at',
        'updated_at',
    )
    list_filter = ('status',)
    search_fields = ('user__email', 'user__username')
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('-created_at',)

    def has_add_permission(self, request):
        return False


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = (
        'cart',
        'product',
        'price',
        'quantity',
        'added_at',
    )
    search_fields = ('product__name',)
    readonly_fields = ('added_at',)
    ordering = ('-added_at',)

    def has_add_permission(self, request):
        return False
