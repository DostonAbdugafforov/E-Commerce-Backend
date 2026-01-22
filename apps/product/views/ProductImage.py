from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
)
from rest_framework.parsers import MultiPartParser, FormParser
from apps.product.permissions import IsAdminOrSellerOrReadOnly, IsOwnerOrAdminOrReadOnly

from apps.product.models import ProductImage
from apps.product.serializers.ProductImage import (
    ProductImageSerializer,
    ProductImageDetailSerializer,
    ProductImageCreateSerializer,
    ProductImageUpdateSerializer,
    ProductImageDeleteSerializer,
)


class ProductImageListAPIView(ListAPIView):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer
    permission_classes = [IsAuthenticated]


class ProductImageDetailAPIView(RetrieveAPIView):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageDetailSerializer
    permission_classes = [IsAuthenticated]


class ProductImageCreateAPIView(CreateAPIView):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageCreateSerializer
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = [IsAdminOrSellerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ProductImageUpdateAPIView(UpdateAPIView):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageUpdateSerializer
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = [IsAuthenticated, IsOwnerOrAdminOrReadOnly]


class ProductImageDeleteAPIView(DestroyAPIView):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageDeleteSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrAdminOrReadOnly]




