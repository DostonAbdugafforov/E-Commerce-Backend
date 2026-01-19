from rest_framework import serializers
from sales.models.FlashSale import FlashSale
from django.db.models import Q


class FlashSaleUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlashSale
        fields = [
            'discount_percentage',
            'quantity',
            'start_time',
            'end_time',
            'is_active',
        ]

    def validate(self, attrs):
        instance = self.instance
        product = instance.product
        start_time = attrs.get('start_time', instance.start_time)
        end_time = attrs.get('end_time', instance.end_time)
        quantity = attrs.get('quantity', instance.quantity)
        is_active = attrs.get('is_active', instance.is_active)

        if start_time >= end_time:
            raise serializers.ValidationError({
                'end_time': "Tugash vaqti boshlanish vaqtidan kechroq bo'lishi kerak"
            })

        overlapping = FlashSale.objects.filter(
            product=product,
            is_active=True
        ).filter(
            Q(start_time__lte=end_time) & Q(end_time__gte=start_time)
        ).exclude(pk=instance.pk)

        if overlapping.exists():
            raise serializers.ValidationError(
                "Bu mahsulot uchun berilgan vaqt oralig'ida boshqa flash sale mavjud"
            )

        if quantity < 1:
            raise serializers.ValidationError("Flash sale uchun minimal quantity 1 bo'lishi kerak")

        if not product.is_active:
            raise serializers.ValidationError("Faol bo‘lmagan mahsulot uchun flash sale yaratib bo‘lmaydi")

        if product.stock < quantity:
            raise serializers.ValidationError("Mahsulot stocki yetarli emas")

        return attrs


