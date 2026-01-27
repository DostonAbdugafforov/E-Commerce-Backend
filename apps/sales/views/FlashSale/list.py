from datetime import timedelta

from django.shortcuts import get_object_or_404
from django.utils import timezone
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.analytics.models.ProductViewHistory import ProductViewHistory
from apps.product.models import Product
from apps.sales.models.FlashSale import FlashSale
from apps.sales.serializers.FlashSale.detail import FlashSaleDetailSerializer
from apps.sales.serializers.FlashSale.list import FlashSaleSerializer


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


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def my_interested_flash_sales(request):
    """Foydalanuvchi ko'rgan mahsulotlari uchun flash sale'lar"""
    now = timezone.now()

    viewed_product_ids = ProductViewHistory.objects.filter(
        user=request.user
    ).values_list('product_id', flat=True)

    flash_sales = FlashSale.objects.filter(
        product_id__in=viewed_product_ids,
        start_time__lte=now,
        end_time__gte=now
    ).distinct()

    serializer = FlashSaleSerializer(flash_sales, many=True)

    return Response({
        'count': flash_sales.count(),
        'results': serializer.data
    })


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def check_product_flash_sale(request, product_id):
    """Mahsulotga flashsale bor yo'qligini tekshirish"""
    now = timezone.now()

    product = get_object_or_404(Product, id=product_id)

    flash_sale = FlashSale.objects.filter(
        product=product,
        start_time__lte=now,
        end_time__gte=now
    ).first()

    if flash_sale:
        serializer = FlashSaleDetailSerializer(flash_sale)
        return Response({
            'has_flash_sale': True,
            'type': 'active',
            'message': 'Bu mahsulot uchun hozir flash sale mavjud',
            'flash_sale': serializer.data
        })

    return Response({
        'has_flash_sale': False,
        'message': 'Bu mahsulot uchun flash sale yo‘q'
    })

