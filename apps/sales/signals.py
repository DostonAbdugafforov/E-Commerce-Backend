from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model

from apps.sales.models.FlashSale import FlashSale
from apps.sales.models.FlashSaleNotification import FlashSaleNotification


@receiver(post_save, sender=FlashSale)
def create_flash_sale_notifications(sender, instance, created, **kwargs):
    if created:
        user = get_user_model()
        users = user.objects.all()

        notifications = [
            FlashSaleNotification(
                user=user,
                flash_sale=instance,
                title=f"{instance.product.name} mahsuloti chegirmada",
                description=f"{instance.product.name} mahsuloti uchun chegirma {instance.discount_percentage}%!"
            )
            for user in users
        ]
        FlashSaleNotification.objects.bulk_create(notifications)

