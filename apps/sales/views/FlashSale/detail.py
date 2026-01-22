from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from apps.sales.models.FlashSale import FlashSale
from apps.sales.serializers.FlashSale.detail import FlashSaleDetailSerializer


class FlashSaleDetailAPIView(RetrieveAPIView):
    queryset = FlashSale.objects.select_related('product').all()
    serializer_class = FlashSaleDetailSerializer
    permission_classes = [IsAuthenticated]

