from rest_framework import serializers
from apps.cart.models.Cart import Cart
from apps.cart.serializers.CartItem.list import CartItemSerializer


class ActiveCartDetailSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)
    total_price = serializers.DecimalField(max_digits=12, decimal_places=2, read_only=True)
    total_quantity = serializers.IntegerField(read_only=True)

    class Meta:
        model = Cart
        fields = [
            'id',
            'status',
            'total_price',
            'total_quantity',
            'items'
        ]
        read_only_fields = ['total_price', 'total_quantity', 'items']
