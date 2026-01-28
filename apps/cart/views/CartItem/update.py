from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAuthenticated

from apps.cart.models.CartItem import CartItem
from apps.cart.serializers.CartItem.update import CartItemUpdateSerializer


class CartItemUpdateAPIView(UpdateAPIView):
    serializer_class = CartItemUpdateSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'

    def get_queryset(self):
        """Faqat o'ziga tegishli itemlarni update qilish"""
        return CartItem.objects.filter(cart__user=self.request.user)

