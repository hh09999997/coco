"""
إعدادات مشروع coco باستخدام Django
"""

from pathlib import Path
import os

# 📂 المسار الأساسي للمشروع
BASE_DIR = Path(__file__).resolve().parent.parent

# 🔐 مفاتيح الأمان
SECRET_KEY = 'django-insecure-تأكد-من-تغيير-هذا-المفتاح-في-الإنتاج'

DEBUG = True

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

    # 🌸 تطبيقات المشروع
    'account',
    'shop',
    'dashboard',
]

# ⚙️ الوسائط والبرمجيات الوسيطة
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# 🧭 إعدادات التوجيه
ROOT_URLCONF = 'coco.urls'

# 🎨 إعدادات القوالب (SSR)
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # مجلد القوالب العام
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

# 🗄️ قاعدة البيانات (SQLite افتراضيًا)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# 🔐 نموذج المستخدم المخصص
AUTH_USER_MODEL = 'account.User'

# 🔐 التحقق من كلمات المرور
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# 🌍 اللغة والمنطقة الزمنية
LANGUAGE_CODE = 'ar'
TIME_ZONE = 'Asia/Riyadh'

USE_I18N = True
USE_L10N = True
USE_TZ = True

# 🖼️ الملفات الثابتة
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]

# 📸 الملفات المرفوعة (الوسائط)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# 💬 الإعدادات الافتراضية
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
