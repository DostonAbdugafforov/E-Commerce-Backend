from rest_framework import serializers
from apps.cart.models.CartItem import CartItem


class CartItemSerializer(serializers.ModelSerializer):
    total_price = serializers.DecimalField(max_digits=12, decimal_places=2, read_only=True)

    class Meta:
        model = CartItem
        fields = [
            'id',
            'product',
            'price',
            'quantity',
            'total_price',
            'added_at'
        ]
        read_only_fields = ['price', 'total_price', 'added_at']

