from rest_framework import serializers
from apps.analytics.models import ProductViewHistory


class ProductViewHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductViewHistory
        fields = [
            'id',
            'product',
            'user',
            'created_at',
        ]

