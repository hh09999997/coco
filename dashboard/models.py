from django.db import models
from django.utils.translation import gettext_lazy as _


# 📊 نموذج تقرير المبيعات اليومية
class DailyReport(models.Model):
    report_date = models.DateField(_("تاريخ التقرير"))
    total_sales = models.DecimalField(_("إجمالي المبيعات"), max_digits=10, decimal_places=2)
    total_orders = models.PositiveIntegerField(_("عدد الطلبات"))
    notes = models.TextField(_("ملاحظات"), blank=True, null=True)

    class Meta:
        verbose_name = _("تقرير يومي")
        verbose_name_plural = _("التقارير اليومية")
        ordering = ['-report_date']

    def __str__(self):
        return f"{self.report_date} - {self.total_sales} ريال"
