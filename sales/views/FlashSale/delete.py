from rest_framework.generics import DestroyAPIView
from sales.models.FlashSale import FlashSale


class FlashSaleDeleteAPIView(DestroyAPIView):
    queryset = FlashSale.objects.all()

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.status = 'cancelled'
        instance.save()

