from django.contrib import admin
from .models import Category, Product


# 🏷️ فئة المنتجات
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    ordering = ("name",)


# 👕 المنتجات
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "price", "created_at")
    list_filter = ("category",)
    search_fields = ("name", "description")
    ordering = ("-created_at",)
