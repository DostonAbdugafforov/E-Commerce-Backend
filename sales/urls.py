# from django.urls import path
# from . import views
#
# app_name = 'flash_sales'
#
# urlpatterns = [
#     # CRUD endpoints
#     path('', views.FlashSaleListView.as_view(), name='list'),
#     path('create/', views.FlashSaleCreateView.as_view(), name='create'),
#     path('<int:pk>/', views.FlashSaleDetailView.as_view(), name='detail'),
#     path('<int:pk>/update/', views.FlashSaleUpdateView.as_view(), name='update'),
#     path('<int:pk>/delete/', views.FlashSaleDeleteView.as_view(), name='delete'),
#
#     # Special endpoints
#     path('active/', views.active_flash_sales, name='active'),
#     path('upcoming/', views.upcoming_flash_sales, name='upcoming'),
#     path('my-interested/', views.my_interested_flash_sales, name='my-interested'),
#     path('product/<int:product_id>/check/', views.check_product_flash_sale, name='check-product'),
#     path('product/<int:product_id>/view/', views.record_product_view, name='record-view'),
#
#     # User related
#     path('notifications/', views.my_notifications, name='notifications'),
#     path('view-history/', views.my_view_history, name='view-history'),
# ]