# from rest_framework import serializers
# from .models import FlashSale
#
#
# class FlashSaleSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = FlashSale
#         fields = [
#             'id',
#             'product',
#             'discount_percentage',
#             'start_time',
#             'end_time',
#         ]


# from rest_framework import serializers
# from django.utils import timezone
# from .models import FlashSale, FlashSaleNotification, ProductViewHistory
# from product.serializers import ProductSerializer
#
#
# class FlashSaleSerializer(serializers.ModelSerializer):
#     product_name = serializers.CharField(source='product.name', read_only=True)
#     remaining_quantity = serializers.IntegerField(read_only=True)
#     is_currently_active = serializers.BooleanField(read_only=True)
#     time_until_start = serializers.SerializerMethodField()
#     time_until_end = serializers.SerializerMethodField()
#     discount_amount = serializers.SerializerMethodField()
#
#     class Meta:
#         model = FlashSale
#         fields = [
#             'id',
#             'product',
#             'product_name',
#             'discount_percentage',
#             'original_price',
#             'sale_price',
#             'quantity',
#             'sold_quantity',
#             'remaining_quantity',
#             'start_time',
#             'end_time',
#             'is_active',
#             'status',
#             'is_currently_active',
#             'time_until_start',
#             'time_until_end',
#             'discount_amount',
#             'created_at',
#             'updated_at',
#         ]
#         read_only_fields = ['sale_price', 'sold_quantity', 'status']
#
#     def get_time_until_start(self, obj):
#         time_delta = obj.time_until_start()
#         if time_delta:
#             return int(time_delta.total_seconds())
#         return None
#
#     def get_time_until_end(self, obj):
#         time_delta = obj.time_until_end()
#         if time_delta:
#             return int(time_delta.total_seconds())
#         return None
#
#     def get_discount_amount(self, obj):
#         return obj.original_price - obj.sale_price
#
#     def validate(self, data):
#         # Vaqtlarni tekshirish
#         if 'start_time' in data and 'end_time' in data:
#             if data['start_time'] >= data['end_time']:
#                 raise serializers.ValidationError({
#                     'end_time': 'Tugash vaqti boshlanish vaqtidan kechroq bo\'lishi kerak'
#                 })
#
#         # Chegirma foizini tekshirish
#         if 'discount_percentage' in data:
#             if data['discount_percentage'] < 1 or data['discount_percentage'] > 99:
#                 raise serializers.ValidationError({
#                     'discount_percentage': 'Chegirma 1 dan 99 gacha bo\'lishi kerak'
#                 })
#
#         return data
#
#
# class FlashSaleDetailSerializer(FlashSaleSerializer):
#     product = ProductSerializer(read_only=True)
#
#     class Meta(FlashSaleSerializer.Meta):
#         fields = FlashSaleSerializer.Meta.fields
#
#
# class FlashSaleListSerializer(serializers.ModelSerializer):
#     """List view uchun minimal serializer"""
#     product_name = serializers.CharField(source='product.name', read_only=True)
#     remaining_quantity = serializers.IntegerField(read_only=True)
#
#     class Meta:
#         model = FlashSale
#         fields = [
#             'id',
#             'product',
#             'product_name',
#             'discount_percentage',
#             'sale_price',
#             'original_price',
#             'remaining_quantity',
#             'start_time',
#             'end_time',
#             'status',
#         ]
#
#
# class FlashSaleCreateUpdateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = FlashSale
#         fields = [
#             'product',
#             'discount_percentage',
#             'original_price',
#             'quantity',
#             'start_time',
#             'end_time',
#             'is_active',
#         ]
#
#     def validate_start_time(self, value):
#         if value < timezone.now():
#             raise serializers.ValidationError(
#                 'Boshlanish vaqti hozirgi vaqtdan oldinroq bo\'lishi mumkin emas'
#             )
#         return value
#
#
# class FlashSaleNotificationSerializer(serializers.ModelSerializer):
#     flash_sale = FlashSaleSerializer(read_only=True)
#
#     class Meta:
#         model = FlashSaleNotification
#         fields = ['id', 'flash_sale', 'is_sent', 'sent_at', 'created_at']
#         read_only_fields = ['is_sent', 'sent_at']
#
#
# class ProductViewHistorySerializer(serializers.ModelSerializer):
#     product_name = serializers.CharField(source='product.name', read_only=True)
#
#     class Meta:
#         model = ProductViewHistory
#         fields = ['id', 'product', 'product_name', 'view_count', 'last_viewed']
#         read_only_fields = ['view_count', 'last_viewed']