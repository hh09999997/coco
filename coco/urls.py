"""
🧭 إعدادات المسارات العامة لمشروع coco
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    # 🎛️ لوحة تحكم Django الافتراضية
    path('admin/', admin.site.urls),

    # 👥 تطبيق الحسابات
    path('account/', include('account.urls')),

    # 📊 تطبيق لوحة التحكم (dashboard)
    path('dashboard/', include('dashboard.urls')),

    # 🛍️ تطبيق المتجر (shop)
    path('shop/', include('shop.urls')),

    # 🏠 الصفحة الرئيسية — تعرض home.html من مجلد templates
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
]

# 🖼️ عرض ملفات الوسائط والملفات الثابتة أثناء التطوير فقط
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
