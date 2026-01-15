from django.db import models
from django.conf import settings

from common.models import BaseModel
from sales.models.FlashSale import FlashSale


class FlashSaleNotification(BaseModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    flash_sale = models.ForeignKey(FlashSale, on_delete=models.CASCADE)
    is_read = models.BooleanField(default=False)

    class Meta:
        unique_together = ('user', 'flash_sale')
        ordering = ['-created_at']

