from django.db import models
from django.conf import settings
from apps.product.models import Product
from apps.common.models import BaseModel


class ProductViewHistory(BaseModel):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='viewed_products'
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='view_histories'
    )

    class Meta:
        db_table = 'product_view_history'
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['user', 'created_at']),
            models.Index(fields=['product', 'created_at']),
        ]
        unique_together = ('user', 'product')

