from django.urls import path
from apps.analytics.views.ProductViewHistory import (
    MyViewedProductsAPIView,
    MostViewedProductsAPIView,
    ProductViewsCountAPIView,
)

urlpatterns = [
    path(
        'products/most-viewed/',
        MostViewedProductsAPIView.as_view(),
        name='most-viewed-products'
    ),
    path(
        'users/me/viewed-products/',
        MyViewedProductsAPIView.as_view(),
        name='my-viewed-products'
    ),
    path(
        'admin/products/<int:product_id>/views-count/',
        ProductViewsCountAPIView.as_view(),
        name='product-views-count'
    ),
]

