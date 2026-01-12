# from django.conf import settings
# from django.db import models
# from common.models import BaseModel
#
#
# class Cart(BaseModel):
#     STATUS_CHOICES = (
#         ('active', 'Active'),
#         ('ordered', 'Ordered'),
#         ('abandoned', 'Abandoned'),
#     )
#
#     user = models.ForeignKey(
#         settings.AUTH_USER_MODEL,
#         on_delete=models.CASCADE,
#         related_name='carts'
#     )
#     status = models.CharField(
#         max_length=20,
#         choices=STATUS_CHOICES,
#         default='active'
#     )
#
#     class Meta:
#         indexes = [
#             models.Index(fields=['user', 'status']),
#         ]
#
#     @property
#     def total_price(self):
#         return sum(item.total_price for item in self.items.all())
#
#     @property
#     def total_quantity(self):
#         return sum(item.quantity for item in self.items.all())
#
#     def __str__(self):
#         return f"Cart #{self.id} ({self.user})"
#
#
# class CartItem(models.Model):
#     cart = models.ForeignKey(
#         Cart,
#         on_delete=models.CASCADE,
#         related_name='items'
#     )
#     product = models.ForeignKey(
#         'products.Product',
#         on_delete=models.CASCADE,
#         related_name='cart_items'
#     )
#
#     price = models.DecimalField(
#         max_digits=12,
#         decimal_places=2
#     )
#     quantity = models.PositiveIntegerField(default=1)
#     added_at = models.DateTimeField(auto_now_add=True)
#
#     class Meta:
#         unique_together = ('cart', 'product')
#         indexes = [
#             models.Index(fields=['cart', 'product']),
#         ]
#
#     @property
#     def total_price(self):
#         return self.price * self.quantity
#
#     def __str__(self):
#         return f"{self.product} x {self.quantity}"
