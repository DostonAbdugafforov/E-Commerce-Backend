from rest_framework import serializers
from sales.models.FlashSale import FlashSale


class FlashSaleSerializer(serializers.ModelSerializer):
    product_id = serializers.IntegerField(source='product.id', read_only=True)
    is_currently_active = serializers.SerializerMethodField()

    class Meta:
        model = FlashSale
        fields = [
            'id',
            'product_id',
            'discount_percentage',
            'sale_price',
            'quantity',
            'sold_quantity',
            'start_time',
            'end_time',
            'is_active',
            'status',
            'is_currently_active',
        ]
        read_only_fields = [
            'sale_price',
            'sold_quantity',
            'status',
        ]

    def get_is_currently_active(self, obj):
        return obj.is_currently_active()

