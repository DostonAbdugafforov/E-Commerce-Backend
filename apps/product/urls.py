from django.urls import path
from apps.product.views.Product import (
    ProductListAPIView,
    ProductCreateAPIView,
    ProductDetailAPIView,
    ProductUpdateAPIView,
    ProductDestroyAPIView,
)
from apps.product.views.ProductImage import (
    ProductImageListAPIView,
    ProductImageDetailAPIView,
    ProductImageCreateAPIView,
    ProductImageUpdateAPIView,
    ProductImageDeleteAPIView,
)

urlpatterns = [
    path('product/', ProductListAPIView.as_view()),
    path('product/<int:pk>/detail', ProductDetailAPIView.as_view()),
    path('product/create', ProductCreateAPIView.as_view()),
    path('product/<int:pk>/update', ProductUpdateAPIView.as_view()),
    path('product/<int:pk>/destroy', ProductDestroyAPIView.as_view()),

    path('product/image', ProductImageListAPIView.as_view()),
    path('product/image/<int:pk>/detail', ProductImageDetailAPIView.as_view()),
    path('product/image/create', ProductImageCreateAPIView.as_view()),
    path('product/image/<int:pk>/update', ProductImageUpdateAPIView.as_view()),
    path('product/image/<int:pk>/delete', ProductImageDeleteAPIView.as_view()),
]

