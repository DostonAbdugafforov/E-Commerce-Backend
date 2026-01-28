from rest_framework import serializers
from apps.cart.models.CartItem import CartItem

class CartItemCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = CartItem
        fields = ['product', 'quantity', 'price']
        read_only_fields = ['price']

    def validate(self, attrs):
        product = attrs.get('product')
        quantity = attrs.get('quantity', 1)

        """Mahsulot stock ni tekshirish"""
        if quantity > product.stock:
            raise serializers.ValidationError(
                f"'{product.name}' mahsulot stokda faqat {product.stock} ta mavjud"
            )
        return attrs

    def create(self, validated_data):
        user = self.context['request'].user
        from apps.cart.models.Cart import Cart

        cart, _ = Cart.objects.get_or_create(user=user, status=Cart.Status.ACTIVE)
        product = validated_data['product']
        quantity = validated_data.get('quantity', 1)
        price = product.price

        """Savatda mahsulot allaqachon bor bo'lsa update qiladi"""
        item, created = CartItem.objects.get_or_create(
            cart=cart,
            product=product,
            defaults={'quantity': quantity, 'price': price}
        )
        if not created:
            new_quantity = item.quantity + quantity
            if new_quantity > product.stock:
                raise serializers.ValidationError(
                    f"'{product.name}' mahsulot stokda faqat {product.stock} ta mavjud"
                )
            item.quantity = new_quantity
            item.save()
        return item
