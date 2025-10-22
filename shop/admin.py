from django.contrib import admin
from .models import Category, Product
from django.utils.translation import gettext_lazy as _


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)
    fieldsets = (
        (_("معلومات الفئة"), {"fields": ("name", "description")}),
    )


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'stock', 'created_at')
    list_filter = ('category', 'created_at')
    search_fields = ('name', 'description')
    ordering = ('-created_at',)
    fieldsets = (
        (_("معلومات المنتج"), {"fields": ("name", "category", "description")}),
        (_("التفاصيل المالية والمخزون"), {"fields": ("price", "stock")}),
        (_("معلومات إضافية"), {"fields": ("created_at",)}),
    )
    readonly_fields = ('created_at',)
