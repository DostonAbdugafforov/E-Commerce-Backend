from django.urls import path
from .views import (
    ProductListAPIView,
    ProductCreateAPIView,
    ProductDetailAPIView,
    ProductUpdateAPIView,
    ProductDestroyAPIView,
)

urlpatterns = [
    path('product/', ProductListAPIView.as_view()),
    path('product/<int:pk>/detail', ProductDetailAPIView.as_view()),
    path('product/create', ProductCreateAPIView.as_view()),
    path('product/<int:pk>/update', ProductUpdateAPIView.as_view()),
    path('product/<int:pk>/destroy', ProductDestroyAPIView.as_view()),
]

