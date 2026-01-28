from django.urls import path

from apps.cart.views.Cart.detail import ActiveCartDetailAPIView
from apps.cart.views.Cart.update import ActiveCartUpdateAPIView

from apps.cart.views.CartItem.list import CartItemListAPIView
from apps.cart.views.CartItem.detail import CartItemDetailAPIView
from apps.cart.views.CartItem.create import CartItemCreateAPIView
from apps.cart.views.CartItem.update import CartItemUpdateAPIView
from apps.cart.views.CartItem.delete import CartItemDeleteAPIView


urlpatterns = [
    path('cart/active/', ActiveCartDetailAPIView.as_view(), name='active-cart-detail'),
    path('cart/active/update/', ActiveCartUpdateAPIView.as_view(), name='active-cart-update'),

    path('cart/items/', CartItemListAPIView.as_view(), name='CartItem-list'),
    path('cart/items/<int:id>/detail', CartItemDetailAPIView.as_view(), name='CartItem-detail'),
    path('cart/items/create/', CartItemCreateAPIView.as_view(), name='CartItem-create'),
    path('cart/items/<int:id>/update/', CartItemUpdateAPIView.as_view(), name='CartItem-update'),
    path('cart/items/<int:id>/delete/', CartItemDeleteAPIView.as_view(), name='CartItem-delete'),
]
