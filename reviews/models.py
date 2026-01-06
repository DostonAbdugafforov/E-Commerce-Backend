from django.db import models
from core import settings
from product.models import Product
from common.models import BaseModel


class Review(BaseModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reviews')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    rating = models.PositiveIntegerField()
    content = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.product.name} - {self.rating}'

    class Meta:
        unique_together = ('user', 'product')
        db_table = 'review'
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'
        ordering = ['-id']

