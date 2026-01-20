from django.urls import path
from sales.views.FlashSale.list import FlashSaleListAPIView
from sales.views.FlashSale.detail import FlashSaleDetailAPIView
from sales.views.FlashSale.create import FlashSaleCreateAPIView
from sales.views.FlashSale.update import FlashSaleUpdateAPIView
from sales.views.FlashSale.delete import FlashSaleDeleteAPIView


urlpatterns = [
    path('flash_sales/', FlashSaleListAPIView.as_view(), name='flash_sales-list'),
    path('flash_sales/create/', FlashSaleCreateAPIView.as_view(), name='flash_sales-create'),
    path('flash_sales/<int:pk>/detail/', FlashSaleDetailAPIView.as_view(), name='flash_sales-detail'),
    path('flash_sales/<int:pk>/update/', FlashSaleUpdateAPIView.as_view(), name='flash_sales-update'),
    path('flash_sales/<int:pk>/delete/', FlashSaleDeleteAPIView.as_view(), name='flash_sales-delete'),

    # Special endpoints
    # path('active/', views.active_flash_sales, name='active'),
    # path('upcoming/', views.upcoming_flash_sales, name='upcoming'),
    # path('my-interested/', views.my_interested_flash_sales, name='my-interested'),
    # path('product/<int:product_id>/check/', views.check_product_flash_sale, name='check-product'),
    # path('product/<int:product_id>/view/', views.record_product_view, name='record-view'),

    # User related
    # path('notifications/', views.my_notifications, name='notifications'),
    # path('view-history/', views.my_view_history, name='view-history'),
]
