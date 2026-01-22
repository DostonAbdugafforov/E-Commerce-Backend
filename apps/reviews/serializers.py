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


class ReviewCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = (
            'product',
            'rating',
            'content',
        )

    def validate(self, attrs):
        request = self.context['request']
        user = request.user
        product = attrs['product']

        if Review.objects.filter(user=user, product=product).exists():
            raise serializers.ValidationError(
                {"detail": "Siz bu mahsulotga allaqachon rating bergansiz"}
            )

        return attrs

    def validate_rating(self, value):
        if value < 1 or value > 5:
            raise serializers.ValidationError("Rating 1 dan 5 gacha bo‘lishi kerak")
        return value


class ReviewUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = (
            'rating',
            'content',
        )

    def validate_rating(self, value):
        if value < 1 or value > 5:
            raise serializers.ValidationError("Rating 1 dan 5 gacha bo‘lishi kerak")
        return value


class ReviewDeleteSerializer(ReviewSerializer):
    pass



