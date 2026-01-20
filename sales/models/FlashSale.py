from django.conf import settings
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone

from common.models import BaseModel
from product.models import Product
from django.core.exceptions import ValidationError


class FlashSale(BaseModel):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='flash_sales'
    )
    discount_percentage = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(99)],
        help_text="Chegirma foizi (1-99)"
    )
    sale_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text="Chegirmadagi narx"
    )
    quantity = models.PositiveIntegerField(
        default=0,
        help_text="Chegirma uchun mavjud mahsulot soni"
    )
    sold_quantity = models.PositiveIntegerField(
        default=0,
        help_text="Sotilgan mahsulotlar soni"
    )
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    is_active = models.BooleanField(default=True)

    STATUS_CHOICES = (
        ('scheduled', 'Rejalashtirilgan'),
        ('active', 'Faol'),
        ('expired', 'Tugagan'),
        ('cancelled', 'Bekor qilingan'),
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='scheduled'
    )
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                              related_name='flash_sales', null=True, blank=True)

    def clean(self):
        if self.start_time and self.end_time:
            if self.start_time >= self.end_time:
                raise ValidationError({
                    'end_time': 'Tugash vaqti boshlanish vaqtidan kechroq bo\'lishi kerak'
                })

            # Bir xil mahsulot uchun vaqt oralig'ida boshqa flash sale borligini tekshirish
            overlapping = FlashSale.objects.filter(
                product=self.product,
                is_active=True
            ).filter(
                models.Q(start_time__lte=self.end_time) &
                models.Q(end_time__gte=self.start_time)
            )

            if self.pk:
                overlapping = overlapping.exclude(pk=self.pk)

            if overlapping.exists():
                raise ValidationError(
                    'Bu mahsulot uchun berilgan vaqt oralig\'ida boshqa flash sale mavjud'
                )

    def update_status(self):
        """Statusni hozirgi vaqtga qarab yangilash"""
        now = timezone.now()

        if not self.is_active:
            self.status = 'cancelled'
        elif now < self.start_time:
            self.status = 'scheduled'
        elif self.start_time <= now <= self.end_time:
            if self.quantity > 0 and self.sold_quantity < self.quantity:
                self.status = 'active'
            else:
                self.status = 'expired'
        else:
            self.status = 'expired'

    def save(self, *args, **kwargs):
        # Chegirmali narxni hisoblash
        if self.product.price and self.discount_percentage:
            discount_amount = (self.product.price * self.discount_percentage) / 100
            self.sale_price = self.product.price - discount_amount

        # Statusni avtomatik yangilash
        self.update_status()

        self.full_clean()
        super().save(*args, **kwargs)

    def remaining_quantity(self):
        """Qolgan mahsulotlar soni"""
        return max(0, self.quantity - self.sold_quantity)

    def is_currently_active(self):
        """Flash sale hozir faol yoki yo'qligini tekshirish"""
        self.update_status()
        return self.status == 'active' and self.is_active

    def is_sold_out(self):
        """Mahsulotlar tugaganligini tekshirish"""
        return self.sold_quantity >= self.quantity

    def __str__(self):
        return f"{self.product.name} - {self.discount_percentage}% off"

    class Meta:
        db_table = 'flash_sale'
        verbose_name = 'Flash Sale'
        verbose_name_plural = 'Flash Sales'
        ordering = ['-start_time']
        indexes = [
            models.Index(fields=['start_time', 'end_time']),
            models.Index(fields=['status', 'is_active']),
        ]






