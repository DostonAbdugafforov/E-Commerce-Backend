from rest_framework import serializers
from apps.sales.models.FlashSale import FlashSale
from django.db.models import Q


class FlashSaleCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlashSale
        fields = [
            'product',
            'discount_percentage',
            'quantity',
            'start_time',
            'end_time',
        ]

    def validate(self, attrs):
        product = attrs.get('product')
        start_time = attrs.get('start_time')
        end_time = attrs.get('end_time')

        if start_time and end_time and start_time >= end_time:
            raise serializers.ValidationError({
                'end_time': "Tugash vaqti boshlanish vaqtidan kechroq bo'lishi kerak"
            })

        overlapping = FlashSale.objects.filter(
            product=product,
            is_active=True
        ).filter(
            Q(start_time__lte=end_time) & Q(end_time__gte=start_time)
        )

        if overlapping.exists():
            raise serializers.ValidationError(
                "Bu mahsulot uchun berilgan vaqt oralig'ida boshqa flash sale mavjud"
            )

        if attrs['quantity'] < 1:
            raise serializers.ValidationError("Flash sale uchun minimal quantity 1 bo'lishi kerak")

        if product.stock < attrs['quantity']:
            raise serializers.ValidationError("Mahsulot stocki yetarli emas")

        return attrs

