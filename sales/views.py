# from rest_framework import generics, status, filters
# from rest_framework.decorators import api_view, permission_classes
# from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated, IsAdminUser
# from django_filters.rest_framework import DjangoFilterBackend
# from django.utils import timezone
# from datetime import timedelta
#
# from .models import FlashSale, FlashSaleNotification, ProductViewHistory
# from .serializers import (
#     FlashSaleSerializer,
#     FlashSaleDetailSerializer,
#     FlashSaleListSerializer,
#     FlashSaleCreateUpdateSerializer,
#     FlashSaleNotificationSerializer,
#     ProductViewHistorySerializer
# )
# from .services import FlashSaleService
# from .permissions import IsAdminOrReadOnly
#
#
# # ==================== Flash Sale CRUD Views ====================
#
# class FlashSaleListView(generics.ListAPIView):
#     """
#     Flash sale'lar ro'yxati
#     Filtrlar: status, is_active, product
#     """
#     serializer_class = FlashSaleListSerializer
#     permission_classes = [IsAuthenticated]
#     filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
#     filterset_fields = ['status', 'is_active', 'product']
#     search_fields = ['product__name']
#     ordering_fields = ['start_time', 'discount_percentage', 'created_at']
#     ordering = ['-start_time']
#
#     def get_queryset(self):
#         return FlashSale.objects.select_related('product').all()
#
#
# class FlashSaleDetailView(generics.RetrieveAPIView):
#     """Flash sale tafsilotlari"""
#     queryset = FlashSale.objects.select_related('product').all()
#     serializer_class = FlashSaleDetailSerializer
#     permission_classes = [IsAuthenticated]
#
#
# class FlashSaleCreateView(generics.CreateAPIView):
#     """Yangi flash sale yaratish (faqat admin)"""
#     serializer_class = FlashSaleCreateUpdateSerializer
#     permission_classes = [IsAdminUser]
#
#     def perform_create(self, serializer):
#         flash_sale = serializer.save()
#         # Foydalanuvchilarga xabarnoma yaratish
#         FlashSaleService.create_notification_for_users(flash_sale)
#
#
# class FlashSaleUpdateView(generics.UpdateAPIView):
#     """Flash sale'ni yangilash (faqat admin)"""
#     queryset = FlashSale.objects.all()
#     serializer_class = FlashSaleCreateUpdateSerializer
#     permission_classes = [IsAdminUser]
#
#
# class FlashSaleDeleteView(generics.DestroyAPIView):
#     """Flash sale'ni o'chirish (faqat admin)"""
#     queryset = FlashSale.objects.all()
#     permission_classes = [IsAdminUser]
#
#     def perform_destroy(self, instance):
#         # To'g'ridan-to'g'ri o'chirish o'rniga faolsizlantirish
#         instance.is_active = False
#         instance.status = 'cancelled'
#         instance.save()
#
#
# # ==================== Special Flash Sale Views ====================
#
# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def active_flash_sales(request):
#     """Hozir faol bo'lgan barcha flash sale'lar"""
#     flash_sales = FlashSaleService.get_active_flash_sales()
#     serializer = FlashSaleListSerializer(flash_sales, many=True)
#     return Response({
#         'count': len(flash_sales),
#         'results': serializer.data
#     })
#
#
# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def upcoming_flash_sales(request):
#     """Yaqin vaqtda boshlanadigan flash sale'lar"""
#     hours = int(request.query_params.get('hours', 24))
#     flash_sales = FlashSaleService.get_upcoming_flash_sales(hours=hours)
#     serializer = FlashSaleListSerializer(flash_sales, many=True)
#     return Response({
#         'count': len(flash_sales),
#         'results': serializer.data
#     })
#
#
# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def my_interested_flash_sales(request):
#     """Foydalanuvchi ko'rgan mahsulotlar uchun flash sale'lar"""
#     hours = int(request.query_params.get('hours', 24))
#     flash_sales = FlashSaleService.get_user_interested_flash_sales(
#         user=request.user,
#         hours=hours
#     )
#     serializer = FlashSaleDetailSerializer(flash_sales, many=True)
#     return Response({
#         'count': len(flash_sales),
#         'results': serializer.data
#     })
#
#
# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def check_product_flash_sale(request, product_id):
#     """
#     Mahsulot uchun flash sale mavjudligini tekshirish
#     """
#     result = FlashSaleService.check_product_flash_sale(
#         product_id=product_id,
#         user=request.user
#     )
#
#     if result:
#         serializer = FlashSaleDetailSerializer(result['flash_sale'])
#         return Response({
#             'has_flash_sale': True,
#             'type': result['type'],
#             'message': result['message'],
#             'flash_sale': serializer.data
#         })
#     else:
#         return Response({
#             'has_flash_sale': False,
#             'message': 'Bu mahsulot uchun flash sale yo\'q'
#         })
#
#
# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def record_product_view(request, product_id):
#     """Mahsulot ko'rilganini qayd qilish"""
#     from product.models import Product
#
#     try:
#         product = Product.objects.get(id=product_id)
#     except Product.DoesNotExist:
#         return Response(
#             {'error': 'Mahsulot topilmadi'},
#             status=status.HTTP_404_NOT_FOUND
#         )
#
#     view = FlashSaleService.record_product_view(request.user, product)
#
#     # Flash sale mavjudligini tekshirish
#     flash_sale_info = FlashSaleService.check_product_flash_sale(
#         product_id=product_id,
#         user=request.user
#     )
#
#     response_data = {
#         'message': 'Ko\'rish qayd qilindi'
#     }
#
#     if flash_sale_info:
#         serializer = FlashSaleDetailSerializer(flash_sale_info['flash_sale'])
#         response_data['flash_sale'] = {
#             'type': flash_sale_info['type'],
#             'message': flash_sale_info['message'],
#             'details': serializer.data
#         }
#
#     return Response(response_data)
#
#
# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def my_notifications(request):
#     """Foydalanuvchining flash sale xabarnmalari"""
#     notifications = FlashSaleNotification.objects.filter(
#         user=request.user
#     ).select_related('flash_sale', 'flash_sale__product').order_by('-created_at')
#
#     serializer = FlashSaleNotificationSerializer(notifications, many=True)
#     return Response({
#         'count': notifications.count(),
#         'results': serializer.data
#     })
#
#
# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def my_view_history(request):
#     """Foydalanuvchi ko'rgan mahsulotlar tarixi"""
#     history = ProductViewHistory.objects.filter(
#         user=request.user
#     ).select_related('product').order_by('-last_viewed')
#
#     serializer = ProductViewHistorySerializer(history, many=True)
#     return Response({
#         'count': history.count(),
#         'results': serializer.data
#     })