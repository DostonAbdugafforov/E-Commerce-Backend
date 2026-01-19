from rest_framework.generics import RetrieveAPIView
from sales.models.FlashSale import FlashSale
from sales.serializers.FlashSale.detail import FlashSaleDetailSerializer


class FlashSaleDetailAPIView(RetrieveAPIView):
    queryset = FlashSale.objects.select_related('product').all()
    serializer_class = FlashSaleDetailSerializer
