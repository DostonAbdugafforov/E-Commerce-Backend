from django.db import transaction

from apps.cart.models import Cart
from apps.order.models import Order, OrderItem


@transaction.atomic
def create_order_from_cart(cart: Cart):
    cart_items = cart.items.all()
    if not cart_items.exists():
        raise ValueError("Cart bo'sh, order yaratib bo'lmaydi")

    order = Order.objects.create(user=cart.user)

    order_items = []
    for item in cart_items:
        order_items.append(
            OrderItem(
                order=order,
                product=item.product,
                price=item.product.price,
                quantity=item.quantity
            )
        )

    OrderItem.objects.bulk_create(order_items)

    return order

