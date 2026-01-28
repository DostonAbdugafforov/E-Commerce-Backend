from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated

from apps.cart.serializers.CartItem.create import CartItemCreateSerializer


class CartItemCreateAPIView(CreateAPIView):
    serializer_class = CartItemCreateSerializer
    permission_classes = [IsAuthenticated]

