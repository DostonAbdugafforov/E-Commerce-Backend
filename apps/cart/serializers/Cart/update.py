from rest_framework import serializers
from apps.cart.models.Cart import Cart

class ActiveCartUpdateSerializer(serializers.ModelSerializer):
    status = serializers.ChoiceField(choices=[Cart.Status.ORDERED, Cart.Status.ABANDONED])

    class Meta:
        model = Cart
        fields = ['status']

    def validate_status(self, value):
        if value not in [Cart.Status.ORDERED, Cart.Status.ABANDONED]:
            raise serializers.ValidationError("Status faqat 'ordered' yoki 'abandoned' bo'lishi mumkin")
        return value
