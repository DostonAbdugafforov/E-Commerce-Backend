from rest_framework import serializers
from apps.analytics.models.ProductViewHistory import ProductViewHistory


class ProductViewHistorySerializer(serializers.ModelSerializer):
    product_id = serializers.IntegerField(source='product.id')
    product_name = serializers.CharField(source='product.name')
    product_price = serializers.DecimalField(
        source='product.price',
        max_digits=10,
        decimal_places=2
    )
    viewed_at = serializers.DateTimeField(source='created_at')

    class Meta:
        model = ProductViewHistory
        fields = (
            'product_id',
            'product_name',
            'product_price',
            'viewed_at',
        )


class MostViewedProductsSerializer(ProductViewHistorySerializer):
    views_count = serializers.IntegerField(read_only=True)

    class Meta(ProductViewHistorySerializer.Meta):
        fields = ProductViewHistorySerializer.Meta.fields + ('views_count',)


class ProductViewsCountSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()
    views_count = serializers.IntegerField()

