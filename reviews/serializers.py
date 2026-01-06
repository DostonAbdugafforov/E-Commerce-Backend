from rest_framework import serializers
from .models import Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = (
            'id',
            'user',
            'product',
            'rating',
            'content',
        )


class ReviewDetailSerializer(ReviewSerializer):
    pass


class ReviewCreateSerializer(ReviewSerializer):
    def validate_rating(self, value):
        if value < 1 or value > 5:
            raise serializers.ValidationError("Rating 1 dan 5 gacha bo‘lishi kerak")
        return value


class ReviewUpdateSerializer(ReviewSerializer):
    def validate_rating(self, value):
        if value < 1 or value > 5:
            raise serializers.ValidationError("Rating 1 dan 5 gacha bo‘lishi kerak")
        return value


class ReviewDeleteSerializer(ReviewSerializer):
    pass



