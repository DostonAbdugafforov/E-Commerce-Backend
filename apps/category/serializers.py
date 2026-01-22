from rest_framework import serializers
from .models import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id','name')


class CategoryDetailSerializer(CategorySerializer):
    pass


class CategoryCreateSerializer(CategorySerializer):
    pass


class CategoryUpdateSerializer(CategorySerializer):
    pass


class CategoryDeleteSerializer(CategorySerializer):
    pass