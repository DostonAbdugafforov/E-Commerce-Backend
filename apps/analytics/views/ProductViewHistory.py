from django.db.models import Count
from drf_yasg.utils import swagger_auto_schema

from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from apps.product.permissions import IsAdminOrSellerOrReadOnly

from apps.product.models import Product

from apps.analytics.models.ProductViewHistory import ProductViewHistory
from apps.analytics.serializers.ProductViewHistory import (
    ProductViewHistorySerializer,
    MostViewedProductsSerializer,
    ProductViewsCountSerializer,
)


class MostViewedProductsAPIView(ListAPIView):
    serializer_class = MostViewedProductsSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Product.objects.annotate(
            views_count=Count('view_histories')
        ).order_by('-views_count')


class MyViewedProductsAPIView(ListAPIView):
    serializer_class = ProductViewHistorySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return ProductViewHistory.objects.filter(
            user=self.request.user
        ).select_related('product').order_by('-created_at')


class ProductViewsCountAPIView(APIView):
    permission_classes = [IsAdminOrSellerOrReadOnly]

    @swagger_auto_schema(responses={200: ProductViewsCountSerializer})
    def get(self, request, product_id):
        count = ProductViewHistory.objects.filter(product_id=product_id).count()
        return Response({
            "product_id": product_id,
            "views_count": count
        })

