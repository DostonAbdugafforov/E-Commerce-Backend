from rest_framework.generics import DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from sales.models.FlashSale import FlashSale
from product.permissions import IsOwnerOrAdminOrReadOnly


class FlashSaleDeleteAPIView(DestroyAPIView):
    queryset = FlashSale.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerOrAdminOrReadOnly]

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.status = 'cancelled'
        instance.save()

