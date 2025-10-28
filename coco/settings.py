"""
⚙️ إعدادات مشروع coco باستخدام Django (بيئة تطوير + إنتاج)
"""

from pathlib import Path
import os
from dotenv import load_dotenv
import cloudinary

# =====================================================
# 📂 المسار الأساسي للمشروع
# =====================================================
BASE_DIR = Path(__file__).resolve().parent.parent

# =====================================================
# 🔐 تحميل متغيرات البيئة من ملف .env
# =====================================================
load_dotenv(BASE_DIR / ".env")

# =====================================================
# 🔧 إعدادات عامة
# =====================================================
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", "django-insecure-تأكد-من-تغييره-في-الإنتاج")

# ⚙️ وضع التشغيل: True = تطوير / False = إنتاج
DEBUG = os.getenv("DEBUG", "True").lower() == "true"

# 🌍 المضيفون المسموح بهم
ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "127.0.0.1,localhost").split(",")

# 🌐 نوع البيئة
ENV = os.getenv("ENV", "development").lower()

# =====================================================
# 🧩 التطبيقات المثبتة
# =====================================================
INSTALLED_APPS = [
    # 🧱 تطبيقات Django الافتراضية
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # ☁️ Cloudinary للتخزين السحابي
    'cloudinary',
    'cloudinary_storage',

    # 🌸 تطبيقات المشروع
    'account.apps.AccountConfig',
    'shop.apps.ShopConfig',
    'dashboard.apps.DashboardConfig',
]

# =====================================================
# ⚙️ البرمجيات الوسيطة (Middleware)
# =====================================================
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# =====================================================
# 🧭 ملف التوجيهات
# =====================================================
ROOT_URLCONF = 'coco.urls'

# =====================================================
# 🎨 إعدادات القوالب (Templates)
# =====================================================
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # 📁 مجلد القوالب الرئيسي
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

# =====================================================
# ⚙️ واجهة WSGI
# =====================================================
WSGI_APPLICATION = 'coco.wsgi.application'

# =====================================================
# 🗄️ قاعدة البيانات (محلية + إنتاج)
# =====================================================
if ENV == "production":
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.getenv("DB_NAME"),
            'USER': os.getenv("DB_USER"),
            'PASSWORD': os.getenv("DB_PASSWORD"),
            'HOST': os.getenv("DB_HOST"),
            'PORT': os.getenv("DB_PORT", "5432"),
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

# =====================================================
# 👤 نموذج المستخدم المخصص
# =====================================================
AUTH_USER_MODEL = 'account.User'

# =====================================================
# 🔐 إعدادات كلمات المرور
# =====================================================
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', 'OPTIONS': {'min_length': 8}},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# =====================================================
# 🌍 اللغة والمنطقة الزمنية
# =====================================================
LANGUAGE_CODE = 'ar'
TIME_ZONE = 'Asia/Riyadh'
USE_I18N = True
USE_TZ = True

# 🌐 اللغات المدعومة
LANGUAGES = [
    ('ar', 'العربية'),
    ('en', 'English'),
]
LOCALE_PATHS = [BASE_DIR / 'locale']

# =====================================================
# 🖼️ الملفات الثابتة والميديا
# =====================================================
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'  # 📦 مجلد التجميع للإنتاج

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# =====================================================
# ☁️ إعدادات Cloudinary
# =====================================================
cloudinary.config(
    cloud_name=os.getenv("CLOUDINARY_CLOUD_NAME"),
    api_key=os.getenv("CLOUDINARY_API_KEY"),
    api_secret=os.getenv("CLOUDINARY_API_SECRET"),
)

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

# =====================================================
# 💬 إعدادات عامة إضافية
# =====================================================
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ✅ معلومات لسهولة التتبع في لوحة التحكم
print(f"🚀 البيئة الحالية: {ENV.upper()} | قاعدة البيانات: {DATABASES['default']['ENGINE']}")
