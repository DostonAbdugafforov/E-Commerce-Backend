from rest_framework.generics import CreateAPIView
from sales.models.FlashSale import FlashSale
from sales.serializers.FlashSale.create import FlashSaleCreateSerializer


class FlashSaleCreateAPIView(CreateAPIView):
    queryset = FlashSale.objects.all()
    serializer_class = FlashSaleCreateSerializer
