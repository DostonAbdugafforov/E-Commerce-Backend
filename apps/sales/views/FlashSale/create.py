from rest_framework.generics import CreateAPIView
from apps.sales.models.FlashSale import FlashSale
from apps.sales.serializers.FlashSale.create import FlashSaleCreateSerializer
from apps.product.permissions import IsAdminOrSellerOrReadOnly


class FlashSaleCreateAPIView(CreateAPIView):
    queryset = FlashSale.objects.all()
    serializer_class = FlashSaleCreateSerializer
    permission_classes = [IsAdminOrSellerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

