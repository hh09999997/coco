from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from django.utils.translation import gettext_lazy as _


# 👤 تخصيص عرض المستخدم في لوحة التحكم
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ("username", "email", "first_name", "last_name", "phone", "is_staff")
    search_fields = ("username", "email", "phone")
    list_filter = ("is_staff", "is_active", "is_superuser")
    ordering = ("username",)

    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("المعلومات الشخصية"), {"fields": ("first_name", "last_name", "email", "phone", "address")}),
        (_("الصلاحيات"), {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
        (_("التواريخ"), {"fields": ("last_login", "date_joined")}),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("username", "email", "phone", "address", "password1", "password2", "is_staff", "is_active"),
        }),
    )
