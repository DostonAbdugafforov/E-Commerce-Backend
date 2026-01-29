from rest_framework.exceptions import NotFound
from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.cart.models.Cart import Cart
from apps.cart.serializers.Cart.update import ActiveCartUpdateSerializer
from apps.order.service import create_order_from_cart


class ActiveCartUpdateAPIView(UpdateAPIView):
    serializer_class = ActiveCartUpdateSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        """Foydalanuvchi active cartini olish"""
        try:
            return Cart.objects.get(user=self.request.user, status=Cart.Status.ACTIVE)
        except Cart.DoesNotExist:
            raise NotFound("Foydalanuvchida active cart mavjud emas")

    def patch(self, request, *args, **kwargs):
        cart = self.get_object()
        serializer = self.get_serializer(cart, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        updated_cart = serializer.save()

        """Cart status ordered bolganda order yaratish"""
        if updated_cart.status == Cart.Status.ORDERED:
            create_order_from_cart(updated_cart)

        return Response(self.get_serializer(updated_cart).data)
