from rest_framework import serializers
from apps.sales.models.FlashSale import FlashSale
from apps.product.models import Product



class ProductNestedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'price'
        ]


class FlashSaleDetailSerializer(serializers.ModelSerializer):
    product = ProductNestedSerializer(read_only=True)
    remaining_quantity = serializers.SerializerMethodField()
    is_sold_out = serializers.SerializerMethodField()

    class Meta:
        model = FlashSale
        fields = [
            'id',
            'product',
            'discount_percentage',
            'sale_price',
            'quantity',
            'sold_quantity',
            'remaining_quantity',
            'start_time',
            'end_time',
            'is_active',
            'status',
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
