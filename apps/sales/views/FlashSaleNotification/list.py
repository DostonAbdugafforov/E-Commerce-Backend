from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from apps.sales.models.FlashSaleNotification import FlashSaleNotification
from apps.sales.serializers.FlashSaleNotification.list import FlashSaleNotificationSerializer


class FlashSaleNotificationListAPIView(ListAPIView):
    serializer_class = FlashSaleNotificationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return FlashSaleNotification.objects.filter(
            user=self.request.user,
            is_read=False
        )


class FlashSaleNotificationUnreadCountAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        count = FlashSaleNotification.objects.filter(
            user=request.user,
            is_read=False
        ).count()
        return Response({"unread_count": count})


