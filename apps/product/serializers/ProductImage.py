from rest_framework import serializers
from apps.product.models import ProductImage


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = [
            'id',
            'product',
            'image',
            'is_main',
        ]


class ProductImageDetailSerializer(ProductImageSerializer):
    pass


class ProductImageCreateSerializer(ProductImageSerializer):
    pass


class ProductImageUpdateSerializer(ProductImageSerializer):
    pass


class ProductImageDeleteSerializer(ProductImageSerializer):
    pass