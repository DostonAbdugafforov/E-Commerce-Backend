from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from apps.cart.models.CartItem import CartItem
from apps.cart.serializers.CartItem.list import CartItemSerializer


class CartItemListAPIView(ListAPIView):
    serializer_class = CartItemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Foydalanuvchining active cartidagi itemlar"""
        return CartItem.objects.filter(cart__user=self.request.user)

