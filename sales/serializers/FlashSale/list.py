from rest_framework import serializers
from sales.models.FlashSale import FlashSale


class FlashSaleSerializer(serializers.ModelSerializer):
    product_id = serializers.IntegerField(source='product.id', read_only=True)
    product_name = serializers.CharField(source='product.name', read_only=True)
    product_price = serializers.DecimalField(
        source='product.price',
        decimal_places=2,
        max_digits=10,
        read_only=True
    )
    is_currently_active = serializers.SerializerMethodField()

    class Meta:
        model = FlashSale
        fields = [
            'id',
            'product_id',
            'product_name',
            'product_price',
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

