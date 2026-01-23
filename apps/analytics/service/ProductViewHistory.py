from django.utils import timezone
from datetime import timedelta

from apps.analytics.models.ProductViewHistory import ProductViewHistory


def track_product_view(user, product):
    """User productni ko‘rganda avtomatik yozish / update"""
    obj, created = ProductViewHistory.objects.get_or_create(
        user=user,
        product=product
    )
    if not created:
        obj.save(update_fields=['created_at'])


def cleanup_old_views(days=30):
    """Eski view history tozalash"""
    ProductViewHistory.objects.filter(
        created_at__lt=timezone.now() - timedelta(days=days)
    ).delete()
