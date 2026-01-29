from rest_framework import serializers
from apps.order.models import Order, OrderItem


class OrderItemSerializer(serializers.ModelSerializer):
    total_amount = serializers.DecimalField(
        max_digits=12, decimal_places=2, read_only=True
    )
    product_name = serializers.CharField(source='product.name', read_only=True)

    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'product_name', 'price', 'quantity', 'total_amount']


class OrderSerializer(serializers.ModelSerializer):
    total_amount = serializers.DecimalField(
        max_digits=12, decimal_places=2, read_only=True
    )

    class Meta:
        model = Order
        fields = ['id', 'order_number', 'status', 'total_amount']


class OrderDetailSerializer(OrderSerializer):
    items = OrderItemSerializer(many=True, read_only=True)

    class Meta(OrderSerializer.Meta):
        fields = OrderSerializer.Meta.fields + ['items']

