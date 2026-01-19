from rest_framework.generics import ListAPIView
from sales.models.FlashSale import FlashSale
from sales.serializers.FlashSale.list import FlashSaleSerializer


class FlashSaleListAPIView(ListAPIView):
    queryset = FlashSale.objects.select_related('product').all()
    serializer_class = FlashSaleSerializer
