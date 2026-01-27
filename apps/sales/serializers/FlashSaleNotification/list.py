from rest_framework import serializers
from apps.sales.models.FlashSaleNotification import FlashSaleNotification


class FlashSaleNotificationSerializer(serializers.ModelSerializer):
    flash_sale_id = serializers.IntegerField(source='flash_sale.id', read_only=True)

    class Meta:
        model = FlashSaleNotification
        fields = (
            'id',
            'title',
            'description',
            'is_read',
            'flash_sale_id',
            'created_at',
        )
