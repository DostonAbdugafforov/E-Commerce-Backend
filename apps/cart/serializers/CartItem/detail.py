from apps.cart.serializers.CartItem.list import CartItemSerializer


class CartItemDetailSerializer(CartItemSerializer):
    class Meta(CartItemSerializer.Meta):
        fields = CartItemSerializer.Meta.fields + ['cart']
        read_only_fields = CartItemSerializer.Meta.read_only_fields + ['cart']


