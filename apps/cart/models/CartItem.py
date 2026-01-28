from django.core.validators import MinValueValidator
from django.db import models
from apps.cart.models.Cart import Cart


class CartItem(models.Model):
    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE,
        related_name='items'
    )
    product = models.ForeignKey(
        'product.Product',
        on_delete=models.PROTECT,
        related_name='cart_items'
    )
    price = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        null=True,
        blank=True
    )
    quantity = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1)])
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('cart', 'product')
        indexes = [
            models.Index(fields=['cart', 'product']),
        ]

    @property
    def total_price(self):
        return self.price * self.quantity

    def save(self, *args, **kwargs):
        """Agar price kiritilmasa avtomatik product ni price ni olib keladi"""
        if not self.price:
            self.price = self.product.price
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.product} x {self.quantity}"

