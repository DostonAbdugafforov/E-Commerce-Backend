from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from apps.cart.models.Cart import Cart
from apps.cart.serializers.Cart.detail import ActiveCartDetailSerializer


class ActiveCartDetailAPIView(RetrieveAPIView):
    serializer_class = ActiveCartDetailSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        """Foydalanuvchi active cartini olish"""
        return Cart.objects.get(user=self.request.user, status=Cart.Status.ACTIVE)

