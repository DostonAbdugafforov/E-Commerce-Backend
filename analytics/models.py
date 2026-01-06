# from django.db import models
# from common.models import BaseModel
# from account.models import CustomUser
# from product.models import Product
#
#
# class ProductViewHistory(BaseModel):
#     user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.product.name
#
#     class Meta:
#         db_table = 'product_view_history'
#         verbose_name = 'Product View History'
#         verbose_name_plural = 'Product View Histories'
#         ordering = ['-id']
#
#
