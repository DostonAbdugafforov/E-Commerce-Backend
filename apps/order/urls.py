from django.urls import path
from .views import OrderListAPIView, OrderDetailAPIView


urlpatterns = [
    path('orders/', OrderListAPIView.as_view()),
    path('orders/<int:id>/detail/', OrderDetailAPIView.as_view()),
]

