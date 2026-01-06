from django.urls import path
from .views import (
    ReviewListAPIView,
    ReviewCreateAPIView,
    ReviewDetailAPIView,
    ReviewUpdateAPIView,
    ReviewDeleteAPIView,
)


urlpatterns = [
    path('reviews/', ReviewListAPIView.as_view()),
    path('reviews/create/', ReviewCreateAPIView.as_view()),
    path('reviews/<int:pk>detail/', ReviewDetailAPIView.as_view()),
    path('reviews/<int:pk>/update/', ReviewUpdateAPIView.as_view()),
    path('reviews/<int:pk>/delete/', ReviewDeleteAPIView.as_view()),
]
