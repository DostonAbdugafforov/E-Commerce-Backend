from datetime import timedelta

from django.utils import timezone
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from sales.models.FlashSale import FlashSale
from sales.serializers.FlashSale.list import FlashSaleSerializer


class FlashSaleListAPIView(ListAPIView):
    queryset = FlashSale.objects.select_related('product').all()
    serializer_class = FlashSaleSerializer
    permission_classes = [IsAuthenticated]


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def active_flash_sales(request):
    """Hozir faol bo'lgan barcha flash sale'lar"""
    flash_sales = [fs for fs in FlashSale.objects.filter(is_active=True) if fs.is_currently_active()]
    serializer = FlashSaleSerializer(flash_sales, many=True)
    return Response({
        'count': len(flash_sales),
        'results': serializer.data
    })


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def upcoming_flash_sales(request):
    """Boshkanishiga 24 soat qolgan mahsulotlarga qo'yilgan flash sale'lar"""
    hours = int(request.query_params.get('hours', 24))
    now = timezone.now()

    flash_sales = FlashSale.objects.filter(
        is_active=True,
        status='scheduled',
        start_time__gt=now,
        start_time__lte=now + timedelta(hours=hours)
    )

    serializer = FlashSaleSerializer(
        flash_sales,
        many=True,
        context={'request': request}
    )

    return Response({
        'count': flash_sales.count(),
        'results': serializer.data
    })


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