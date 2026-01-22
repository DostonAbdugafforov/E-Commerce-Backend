from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAuthenticated

from apps.sales.models.FlashSale import FlashSale
from apps.sales.serializers.FlashSale.update import FlashSaleUpdateSerializer
from apps.product.permissions import IsOwnerOrAdminOrReadOnly


class FlashSaleUpdateAPIView(UpdateAPIView):
    queryset = FlashSale.objects.all()
    serializer_class = FlashSaleUpdateSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrAdminOrReadOnly]

