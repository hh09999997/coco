"""
⚙️ إعدادات مشروع coco باستخدام Django (بيئة تطوير + إنتاج)
"""

from pathlib import Path
import os
from dotenv import load_dotenv
import dj_database_url
import cloudinary

# 📂 المسار الأساسي للمشروع
BASE_DIR = Path(__file__).resolve().parent.parent

# 🔐 تحميل متغيرات البيئة من ملف .env
load_dotenv(BASE_DIR / ".env")

# 🔐 مفتاح الأمان — ⚠️ غيّره في بيئة الإنتاج
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", "django-insecure-تأكد-من-تغيير-هذا-المفتاح-في-الإنتاج")

# ⚙️ وضع التطوير (فعّله محليًا فقط)
DEBUG = os.getenv("DEBUG", "True") == "True"

# 🌐 أسماء النطاقات المسموح بها
ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "*").split(",")

# 🧩 التطبيقات المثبتة
INSTALLED_APPS = [
    # 🧱 تطبيقات Django الافتراضية
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # ☁️ Cloudinary
    'cloudinary',
    'cloudinary_storage',

    # 🌸 تطبيقات المشروع
    'account.apps.AccountConfig',
    'shop.apps.ShopConfig',
    'dashboard.apps.DashboardConfig',
]

# ⚙️ البرمجيات الوسيطة
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

# 🧭 ملف التوجيهات
ROOT_URLCONF = 'coco.urls'

# 🎨 إعداد القوالب
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
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

# 🗄️ قاعدة البيانات — تطوير محلي + إنتاج Render
if os.getenv("ENV") == "production":
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.getenv("DB_NAME"),
            'USER': os.getenv("DB_USER"),
            'PASSWORD': os.getenv("DB_PASSWORD"),
            'HOST': os.getenv("DB_HOST"),
            'PORT': os.getenv("DB_PORT"),
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

# 👤 نموذج المستخدم المخصص
AUTH_USER_MODEL = 'account.User'

# 🔐 إعدادات كلمات المرور
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', 'OPTIONS': {'min_length': 8}},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# 🌍 اللغة والمنطقة الزمنية
LANGUAGE_CODE = 'ar'
TIME_ZONE = 'Asia/Riyadh'
USE_I18N = True
USE_TZ = True

# 🌐 تعدد اللغات
LANGUAGES = [('ar', 'العربية'), ('en', 'English')]
LOCALE_PATHS = [BASE_DIR / 'locale']

# 🖼️ الملفات الثابتة
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

# 📸 ملفات الوسائط
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# ☁️ إعدادات Cloudinary
cloudinary.config(
    cloud_name=os.getenv("CLOUDINARY_CLOUD_NAME"),
    api_key=os.getenv("CLOUDINARY_API_KEY"),
    api_secret=os.getenv("CLOUDINARY_API_SECRET"),
)
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

# 💬 المعرف الافتراضي
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
