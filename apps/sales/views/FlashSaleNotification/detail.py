from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from apps.sales.models.FlashSaleNotification import FlashSaleNotification
from apps.sales.serializers.FlashSaleNotification.list import FlashSaleNotificationSerializer


class FlashSaleNotificationDetailAPIView(RetrieveAPIView):
    queryset = FlashSaleNotification.objects.all()
    serializer_class = FlashSaleNotificationSerializer
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_read = True
        instance.save(update_fields=['is_read'])
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

