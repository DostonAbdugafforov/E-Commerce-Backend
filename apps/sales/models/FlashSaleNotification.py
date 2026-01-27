from django.db import models
from django.conf import settings

from apps.common.models import BaseModel
from apps.sales.models.FlashSale import FlashSale


class FlashSaleNotification(BaseModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    flash_sale = models.ForeignKey(FlashSale, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=200, null=True)
    description = models.TextField(null=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        unique_together = ('user', 'flash_sale')
        ordering = ['-created_at']


