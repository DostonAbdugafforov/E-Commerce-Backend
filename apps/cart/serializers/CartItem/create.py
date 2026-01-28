from rest_framework import serializers
from apps.cart.models.CartItem import CartItem

class CartItemCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = CartItem
        fields = [
            'product',
            'quantity',
            'price'
        ]
        extra_kwargs = {
            'price': {'required': False}
        }

    def create(self, validated_data):
        user = self.context['request'].user
        from apps.cart.models.Cart import Cart

        # Foydalanuvchining active cartini topish yoki yaratish
        cart, _ = Cart.objects.get_or_create(user=user, status=Cart.Status.ACTIVE)
        product = validated_data['product']
        quantity = validated_data.get('quantity', 1)

        # Agar price POST da kiritilmagan bo‘lsa, product.price dan olamiz
        price = validated_data.get('price') or product.price

        # Agar item allaqachon bo‘lsa, quantity update qilinadi
        item, created = CartItem.objects.get_or_create(
            cart=cart,
            product=product,
            defaults={'quantity': quantity, 'price': price}
        )
        if not created:
            item.quantity += quantity
            item.save()
        return item
