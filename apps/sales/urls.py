from django.urls import path
from apps.sales.views.FlashSale.list import (
    FlashSaleListAPIView,
    active_flash_sales,
    upcoming_flash_sales,
    my_interested_flash_sales,
    check_product_flash_sale,
)
from apps.sales.views.FlashSale.detail import FlashSaleDetailAPIView
from apps.sales.views.FlashSale.create import FlashSaleCreateAPIView
from apps.sales.views.FlashSale.update import FlashSaleUpdateAPIView
from apps.sales.views.FlashSale.delete import FlashSaleDeleteAPIView

from apps.sales.views.FlashSaleNotification.list import (FlashSaleNotificationListAPIView,
                                                         FlashSaleNotificationUnreadCountAPIView)
from apps.sales.views.FlashSaleNotification.detail import FlashSaleNotificationDetailAPIView


urlpatterns = [
    path('flash_sales/', FlashSaleListAPIView.as_view(), name='flash_sales-list'),
    path('flash_sales/create/', FlashSaleCreateAPIView.as_view(), name='flash_sales-create'),
    path('flash_sales/<int:pk>/detail/', FlashSaleDetailAPIView.as_view(), name='flash_sales-detail'),
    path('flash_sales/<int:pk>/update/', FlashSaleUpdateAPIView.as_view(), name='flash_sales-update'),
    path('flash_sales/<int:pk>/delete/', FlashSaleDeleteAPIView.as_view(), name='flash_sales-delete'),

    path('active_flash_sales/', active_flash_sales, name='active'),
    path('upcoming_flash_sales/', upcoming_flash_sales, name='upcoming'),
    path('my_interested_flash_sales/', my_interested_flash_sales, name='my-interested'),
    path('product/<int:product_id>/check_flash_sale/', check_product_flash_sale, name='check-product-flash_sale'),

    path('flash_sales/notifications/', FlashSaleNotificationListAPIView.as_view(),
         name='flash_sale-notifications-list'),
    path('flash_sales/notifications/<int:pk>/', FlashSaleNotificationDetailAPIView.as_view(),
         name='flash_sale-notifications-detail'),
    path('flash_sales/notifications/unread-count/', FlashSaleNotificationUnreadCountAPIView.as_view(),
         name='flash_sale-notifications-unread-count'),
]
