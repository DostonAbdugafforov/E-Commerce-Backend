from django.conf import settings
from django.db import models
from django.db.models import Q

from apps.common.models import BaseModel


class Cart(BaseModel):
    class Status(models.TextChoices):
        ACTIVE = 'active', 'Active'
        ORDERED = 'ordered', 'Ordered'
        ABANDONED = 'abandoned', 'Abandoned'

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='carts'
    )
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.ACTIVE
    )

    class Meta:
        indexes = [
            models.Index(fields=['user', 'status']),
        ]
        constraints = [
            models.UniqueConstraint(
                fields=['user'],
                condition=Q(status='active'),
                name='unique_active_cart_per_user'
            )
        ]

    @property
    def total_price(self):
        return sum(item.total_price for item in self.items.all())

    @property
    def total_quantity(self):
        return sum(item.quantity for item in self.items.all())

    def __str__(self):
        return f"Cart #{self.id}"


