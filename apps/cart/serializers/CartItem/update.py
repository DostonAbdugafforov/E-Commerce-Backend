from rest_framework import serializers
from apps.cart.models.CartItem import CartItem


class CartItemUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['quantity']

    def validate_quantity(self, value):
        product = self.instance.product
        if value > product.stock:
            raise serializers.ValidationError(
                f"'{product.name}' mahsulot stokda faqat {product.stock} ta mavjud"
            )
        return value

    def update(self, instance, validated_data):
        instance.quantity = validated_data.get('quantity', instance.quantity)
        instance.save()
        return instance

