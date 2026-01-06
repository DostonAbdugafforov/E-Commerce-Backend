from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'description',
            'category',
            'price',
            'stock',
            'image',
        ]


class ProductDetailSerializer(ProductSerializer):
    pass


class ProductCreateSerializer(ProductSerializer):
    pass


class ProductUpdateSerializer(ProductSerializer):
    pass


class ProductDeleteSerializer(ProductSerializer):
    pass

