from django.db import models
from django.utils.translation import gettext_lazy as _


# 🧾 نموذج لتخزين إحصائيات بسيطة (كمثال أولي)
class DailyReport(models.Model):
    date = models.DateField(_("التاريخ"))
    total_orders = models.PositiveIntegerField(_("عدد الطلبات"), default=0)
    total_sales = models.DecimalField(_("إجمالي المبيعات"), max_digits=10, decimal_places=2, default=0)

    class Meta:
        verbose_name = _("تقرير يومي")
        verbose_name_plural = _("التقارير اليومية")
        ordering = ["-date"]

    def __str__(self):
        return f"تقرير يوم {self.date}"
