"""
⚙️ إعدادات مشروع coco باستخدام Django
"""

from pathlib import Path
import os

# 📂 المسار الأساسي للمشروع
BASE_DIR = Path(__file__).resolve().parent.parent

# 🔐 مفتاح الأمان — ⚠️ غيّره في بيئة الإنتاج
SECRET_KEY = 'django-insecure-تأكد-من-تغيير-هذا-المفتاح-في-الإنتاج'

# ⚙️ وضع التطوير (فعّله محليًا فقط)
DEBUG = True

# 🌐 عند النشر أضف اسم نطاق موقعك هنا
ALLOWED_HOSTS = []

# 🧩 التطبيقات المثبتة
INSTALLED_APPS = [
    # 🧱 تطبيقات Django الافتراضية
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 🌸 تطبيقات المشروع الداخلية
    'account.apps.AccountConfig',
    'shop.apps.ShopConfig',
    'dashboard.apps.DashboardConfig',
]

# ⚙️ البرمجيات الوسيطة (Middleware)
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',  # ✅ دعم تعدد اللغات (العربية والإنجليزية)
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# 🧭 ملف المسارات الأساسية للمشروع
ROOT_URLCONF = 'coco.urls'

# 🎨 إعدادات القوالب (Templates)
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # ✅ تعريف مجلد القوالب العام
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# ⚙️ واجهة WSGI
WSGI_APPLICATION = 'coco.wsgi.application'

# 🗄️ قاعدة البيانات (SQLite الافتراضية)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# 👤 نموذج المستخدم المخصص
AUTH_USER_MODEL = 'account.User'

# 🔐 إعدادات التحقق من كلمات المرور
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {'min_length': 8},  # الحد الأدنى للطول
    },
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# 🌍 اللغة والمنطقة الزمنية
LANGUAGE_CODE = 'ar'
TIME_ZONE = 'Asia/Riyadh'

USE_I18N = True
USE_TZ = True

# 🌐 إعدادات الترجمة
LANGUAGES = [
    ('ar', 'العربية'),
    ('en', 'English'),
]
LOCALE_PATHS = [
    BASE_DIR / 'locale',
]

# 🖼️ الملفات الثابتة (Static)
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static',  # مجلد ملفات التطوير (css, js, img)
]
STATIC_ROOT = BASE_DIR / 'staticfiles'  # مجلد تجميع الملفات عند النشر

# 📸 الملفات المرفوعة (Media)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# 💬 الإعداد الافتراضي لمعرّف الحقول
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
