# from django.conf import settings
# from django.db import models
# from common.models import BaseModel
#
#
# class Order(BaseModel):
#     STATUS_CHOICES = (
#         ('processing', 'Processing'),
#         ('completed', 'Completed'),
#         ('cancelled', 'Cancelled'),
#     )
#
#     user = models.ForeignKey(
#         settings.AUTH_USER_MODEL,
#         on_delete=models.CASCADE,
#         related_name='orders'
#     )
#     order_number = models.CharField(max_length=20, unique=True)
#     total_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
#     discount_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
#     final_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
#     status = models.CharField(
#         max_length=20,
#         choices=STATUS_CHOICES,
#         default='processing'
#     )
#
#     class Meta:
#         ordering = ['-created_at']
#
#     def __str__(self):
#         return f"Order #{self.order_number} ({self.user})"
#
#
# class OrderItem(models.Model):
#     order = models.ForeignKey(
#         Order,
#         on_delete=models.CASCADE,
#         related_name='items'
#     )
#     product = models.ForeignKey(
#         'products.Product',
#         on_delete=models.CASCADE,
#         related_name='order_items'
#     )
#     product_name = models.CharField(max_length=255)
#     quantity = models.PositiveIntegerField(default=1)
#     price = models.DecimalField(max_digits=12, decimal_places=2)
#
#     class Meta:
#         unique_together = ('order', 'product')
#         indexes = [
#             models.Index(fields=['order', 'product']),
#         ]
#
#     @property
#     def total_price(self):
#         return self.price * self.quantity
#
#     def __str__(self):
#         return f"{self.product_name} x {self.quantity}"
