from django.contrib import admin
from .models import DailyReport


# 🧾 التقارير اليومية
@admin.register(DailyReport)
class DailyReportAdmin(admin.ModelAdmin):
    list_display = ("date", "total_orders", "total_sales")
    ordering = ("-date",)
    search_fields = ("date",)
