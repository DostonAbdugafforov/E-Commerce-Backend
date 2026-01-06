from django.urls import path
from .views import (
    CategoryListAPIView,
    CategoryCreateAPIView,
    CategoryUpdateAPIView,
    CategoryDetailAPIView,
    CategoryDeleteAPIView,
)


urlpatterns = [
    path('category/', CategoryListAPIView.as_view()),
    path('category/create/', CategoryCreateAPIView.as_view()),
    path('category/<int:pk>/retrieve/', CategoryDetailAPIView.as_view()),
    path('category/<int:pk>/update/', CategoryUpdateAPIView.as_view()),
    path('category/<int:pk>/delete/', CategoryDeleteAPIView.as_view()),
]
