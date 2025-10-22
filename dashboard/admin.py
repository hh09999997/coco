from django.contrib import admin
from .models import DailyReport
from django.utils.translation import gettext_lazy as _


@admin.register(DailyReport)
class DailyReportAdmin(admin.ModelAdmin):
    list_display = ('report_date', 'total_sales', 'total_orders')
    list_filter = ('report_date',)
    search_fields = ('notes',)
    ordering = ('-report_date',)
    fieldsets = (
        (_('معلومات التقرير'), {
            'fields': ('report_date', 'total_sales', 'total_orders', 'notes')
        }),
    )
