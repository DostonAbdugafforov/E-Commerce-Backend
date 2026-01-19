from rest_framework import serializers
from sales.models.FlashSale import FlashSale


class FlashSaleDetailSerializer(serializers.ModelSerializer):
    product_id = serializers.IntegerField(source='product.id', read_only=True)
    product_name = serializers.CharField(source='product.name', read_only=True)
    product_price = serializers.DecimalField(
        source='product.price',
        decimal_places=2,
        max_digits=10,
        read_only=True
    )
    remaining_quantity = serializers.SerializerMethodField()
    is_currently_active = serializers.SerializerMethodField()
    is_sold_out = serializers.SerializerMethodField()

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
            'remaining_quantity',
            'start_time',
            'end_time',
            'is_active',
            'status',
            'is_currently_active',
            'is_sold_out',
        ]
        read_only_fields = [
            'sale_price',
            'sold_quantity',
            'status',
        ]

        def get_remaining_quantity(self, obj):
            return obj.remaining_quantity()

        def get_is_sold_out(self, obj):
            return obj.is_sold_out()
