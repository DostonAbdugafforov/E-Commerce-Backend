from rest_framework import serializers
from apps.cart.models.Cart import Cart
from apps.order.service import create_order_from_cart


class ActiveCartUpdateSerializer(serializers.ModelSerializer):
    status = serializers.ChoiceField(
        choices=[
            (Cart.Status.ORDERED, "Ordered"),
            (Cart.Status.ABANDONED, "Abandoned")
        ]
    )

    class Meta:
        model = Cart
        fields = ['status']

    def update(self, instance, validated_data):
        new_status = validated_data['status']

        if instance.status == Cart.Status.ACTIVE and new_status == Cart.Status.ORDERED:
            for item in instance.items.select_related('product'):
                product = item.product

                if item.quantity > product.stock:
                    raise serializers.ValidationError(
                        f"'{product.name}' mahsulot stokda yetarli emas"
                    )

            # Stock kamaytirish
            for item in instance.items.select_related('product'):
                product = item.product
                product.stock -= item.quantity
                product.save()

            # Order yaratish
            create_order_from_cart(instance)

        instance.status = new_status
        instance.save()
        return instance
