from rest_framework.exceptions import NotFound
from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAuthenticated

from apps.cart.models.Cart import Cart
from apps.cart.serializers.Cart.update import ActiveCartUpdateSerializer

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
        return self.partial_update(request, *args, **kwargs)
