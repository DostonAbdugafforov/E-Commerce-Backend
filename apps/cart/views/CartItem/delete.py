from rest_framework.generics import DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from apps.cart.models.CartItem import CartItem
from apps.cart.serializers.CartItem.delete import CartItemDeleteSerializer


class CartItemDeleteAPIView(DestroyAPIView):
    serializer_class = CartItemDeleteSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'

    def get_queryset(self):
        """Faqat o'ziga tegishli itemlarni delete qilish"""
        return CartItem.objects.filter(cart__user=self.request.user)

