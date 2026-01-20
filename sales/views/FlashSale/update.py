from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAuthenticated

from sales.models.FlashSale import FlashSale
from sales.serializers.FlashSale.update import FlashSaleUpdateSerializer
from product.permissions import IsOwnerOrAdminOrReadOnly


class FlashSaleUpdateAPIView(UpdateAPIView):
    queryset = FlashSale.objects.all()
    serializer_class = FlashSaleUpdateSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrAdminOrReadOnly]

