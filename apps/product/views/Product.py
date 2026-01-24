from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
)
from rest_framework.response import Response

from apps.analytics.service.ProductViewHistory import track_product_view
from apps.product.permissions import IsAdminOrSellerOrReadOnly, IsOwnerOrAdminOrReadOnly

from apps.product.models import Product
from apps.product.serializers.Product import (
    ProductSerializer,
    ProductCreateSerializer,
    ProductUpdateSerializer,
    ProductDetailSerializer,
    ProductDeleteSerializer,
)


class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]


class ProductCreateAPIView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductCreateSerializer
    permission_classes = [IsAdminOrSellerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ProductDetailAPIView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        track_product_view(request.user, product)
        serializer = self.get_serializer(product)
        return Response(serializer.data)


class ProductUpdateAPIView(UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductUpdateSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrAdminOrReadOnly]


class ProductDestroyAPIView(DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDeleteSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrAdminOrReadOnly]






