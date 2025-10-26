"""
⚙️ إعدادات مشروع coco باستخدام Django — إعداد بيئتي التطوير والإنتاج
"""

from pathlib import Path
import os
from dotenv import load_dotenv
import cloudinary
import cloudinary.uploader
import cloudinary.api

# 📂 المسار الأساسي
BASE_DIR = Path(__file__).resolve().parent.parent

# 🔐 تحميل المتغيرات من ملف .env
load_dotenv(BASE_DIR / ".env")

# 🧩 المفتاح السري
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", "django-insecure-تأكد-من-تغيير-المفتاح-في-الإنتاج")

# ⚙️ وضع التطوير أو الإنتاج
DEBUG = os.getenv("DEBUG", "True").lower() == "true"

# 🌍 المضيفون المسموحون
ALLOWED_HOSTS = ["127.0.0.1", "localhost", "coco.onrender.com", "*"]

# 🧩 التطبيقات المثبتة
INSTALLED_APPS = [
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

# 🧱 الوسائط الوسيطة
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

WSGI_APPLICATION = 'coco.wsgi.application'

# 🗄️ إعداد قاعدة البيانات
if DEBUG:
    # ⚙️ قاعدة بيانات التطوير (محلية SQLite)
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
else:
    # 🗄️ قاعدة بيانات الإنتاج (PostgreSQL على Render)
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'HOST': os.getenv('DB_HOST', 'dpg-d3ilcore5dus73988410-a'),
            'PORT': os.getenv('DB_PORT', '5432'),
            'NAME': os.getenv('DB_NAME', 'db_gdeed'),
            'USER': os.getenv('DB_USER', 'db_gdeed_user'),
            'PASSWORD': os.getenv('DB_PASSWORD', '1QewlrEi3ksgVfQzhC6xrqAIzt7Ybafl'),
            'OPTIONS': {'sslmode': 'require'},
        }
    }

# 👤 نموذج المستخدم المخصص
AUTH_USER_MODEL = 'account.User'

# 🔐 التحقق من كلمات المرور
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
LANGUAGES = [('ar', 'العربية'), ('en', 'English')]
LOCALE_PATHS = [BASE_DIR / 'locale']

# 🖼️ الملفات الثابتة والإعلامية
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# ☁️ إعداد Cloudinary
cloudinary.config(
    cloud_name=os.getenv("CLOUDINARY_CLOUD_NAME", "dxzjjpwko"),
    api_key=os.getenv("CLOUDINARY_API_KEY", "229693619535264"),
    api_secret=os.getenv("CLOUDINARY_API_SECRET", "qwrkahe4W-4C736R2VPxN9cBukU"),
)

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
