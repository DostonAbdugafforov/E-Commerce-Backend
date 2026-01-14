from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from product.models import Product, ProductImage

class ProductSerializer(serializers.ModelSerializer):
    images = SerializerMethodField()

    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'description',
            'category',
            'price',
            'stock',
            'images',
        ]

    def get_images(self, obj):
        images = obj.images.filter(is_main=True)
        return [image.image.url for image in images] if images.exists() else []


class ProductDetailSerializer(ProductSerializer):
    pass


class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'description',
            'category',
            'price',
            'stock',
        ]


class ProductUpdateSerializer(ProductCreateSerializer):
    pass


class ProductDeleteSerializer(ProductSerializer):
    class Meta:
        model = Product
        fields = ['id']