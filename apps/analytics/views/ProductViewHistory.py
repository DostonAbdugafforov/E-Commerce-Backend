from django.shortcuts import get_object_or_404
from django.db.models import Count
from drf_yasg.utils import swagger_auto_schema

from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from apps.product.models import Product

from apps.analytics.models.ProductViewHistory import ProductViewHistory
from apps.analytics.serializers.ProductViewHistory import (
    ProductViewHistorySerializer,
    MostViewedProductsSerializer,
    ProductViewsCountSerializer,
)
from apps.analytics.service.ProductViewHistory import track_product_view



class ProductDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        track_product_view(request.user, product)
        return Response({
            "id": product.id,
            "name": product.name,
            "price": product.price
        })



class MostViewedProductsAPIView(ListAPIView):
    serializer_class = MostViewedProductsSerializer

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
    @swagger_auto_schema(responses={200: ProductViewsCountSerializer})
    def get(self, request, product_id):
        count = ProductViewHistory.objects.filter(product_id=product_id).count()
        return Response({
            "product_id": product_id,
            "views_count": count
        })

