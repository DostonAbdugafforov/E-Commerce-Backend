from rest_framework.generics import UpdateAPIView
from sales.models.FlashSale import FlashSale
from sales.serializers.FlashSale.update import FlashSaleUpdateSerializer


class FlashSaleUpdateAPIView(UpdateAPIView):
    queryset = FlashSale.objects.all()
    serializer_class = FlashSaleUpdateSerializer
