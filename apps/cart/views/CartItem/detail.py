from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from apps.cart.models.CartItem import CartItem
from apps.cart.serializers.CartItem.detail import CartItemDetailSerializer


class CartItemDetailAPIView(RetrieveAPIView):
    serializer_class = CartItemDetailSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'

    def get_queryset(self):
        return CartItem.objects.filter(cart__user=self.request.user)

