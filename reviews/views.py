from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    UpdateAPIView,
    DestroyAPIView,
)
from .models import Review
from .permissions import IsOwnerOrAdminOrReadOnly
from .serializers import (
    ReviewSerializer,
    ReviewCreateSerializer,
    ReviewDetailSerializer,
    ReviewUpdateSerializer,
    ReviewDeleteSerializer,
)


class ReviewListAPIView(ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewCreateAPIView(CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewCreateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ReviewDetailAPIView(RetrieveAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewDetailSerializer


class ReviewUpdateAPIView(UpdateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewUpdateSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrAdminOrReadOnly]


class ReviewDeleteAPIView(DestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewDeleteSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrAdminOrReadOnly]

