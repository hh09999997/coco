from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # 🧭 لوحة تحكم Django الافتراضية
    path('admin/', admin.site.urls),

    # 👥 تطبيق الحسابات
    path('account/', include('account.urls')),

    # 🛍️ تطبيق المتجر
    path('', include('shop.urls')),  # الصفحة الرئيسية مؤقتًا للمتجر

    # 📊 تطبيق لوحة التحكم الإدارية
    path('dashboard/', include('dashboard.urls')),
]
