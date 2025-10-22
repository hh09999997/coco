from django.db import models
from django.utils.translation import gettext_lazy as _


# 🏷️ نموذج الفئة (التصنيف)
class Category(models.Model):
    name = models.CharField(_("اسم الفئة"), max_length=100)
    description = models.TextField(_("الوصف"), blank=True, null=True)

    class Meta:
        verbose_name = _("فئة")
        verbose_name_plural = _("الفئات")

    def __str__(self):
        return self.name


# 👕 نموذج المنتج
class Product(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="products",
        verbose_name=_("الفئة")
    )
    name = models.CharField(_("اسم المنتج"), max_length=150)
    price = models.DecimalField(_("السعر"), max_digits=10, decimal_places=2)
    description = models.TextField(_("الوصف"), blank=True, null=True)
    created_at = models.DateTimeField(_("تاريخ الإضافة"), auto_now_add=True)

    class Meta:
        verbose_name = _("منتج")
        verbose_name_plural = _("المنتجات")
        ordering = ["-created_at"]

    def __str__(self):
        return self.name
