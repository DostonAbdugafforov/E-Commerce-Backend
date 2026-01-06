# from datetime import timezone
#
# from django.db import models
# from common.models import BaseModel
# from product.models import Product
#
#
# class FlashSale(BaseModel):
#     product = models.OneToOneField(Product, on_delete=models.CASCADE)
#     discount_percentage = models.PositiveIntegerField()
#     start_time = models.DateTimeField()
#     end_time = models.DateTimeField()
#
#     def is_active(self):
#         now = timezone.now()
#         return self.start_time <= now <= self.end_time
#
#     def __str__(self):
#         return self.product.name
#
#     class Meta:
#         db_table = 'flash_sale'
#         verbose_name = 'Flash Sale'
#         verbose_name_plural = 'Flash Sales'
#         ordering = ['-id']
#         unique_together = ('product', 'start_time', 'end_time')
#
