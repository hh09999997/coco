from django.contrib import admin
from .models import Product, Category
from django.utils.html import format_html


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'stock', 'show_image')
    list_filter = ('category',)
    search_fields = ('name', 'description')
    readonly_fields = ('show_image',)

    fieldsets = (
        ('📦 معلومات المنتج', {
            'fields': ('name', 'category', 'description', 'price', 'stock', 'image', 'show_image')
        }),
    )

    def show_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="80" height="80" style="border-radius: 8px;"/>', obj.image.url)
        return "لا توجد صورة"
    show_image.short_description = "صورة المنتج"
