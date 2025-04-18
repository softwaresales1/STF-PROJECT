import os
import environ
import dj_database_url
from pathlib import Path

# Initialize environment variables
env = environ.Env(
    DEBUG=(bool, False),
    DJANGO_SECRET_KEY=(str, 'no+5*)qx*oac$5#&)c%a+idhk9-%$*75m1^_w@%kq@cmn2+v3e'),
    DATABASE_URL=(str, ''),
    REDIS_URL=(str, 'redis://localhost:6379/0'),
    EMAIL_HOST_USER=(str, ''),
    EMAIL_HOST_PASSWORD=(str, ''),
)

environ.Env.read_env()  # Load environment variables from .env file if available

# Base directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Security settings
SECRET_KEY = 'no+5*)qx*oac$5#&)c%a+idhk9-%$*75m1^_w@%kq@cmn2+v3e'
DEBUG = False

ALLOWED_HOSTS = [
    'stf-project-0ddq.onrender.com',
    '127.0.0.1',
    'swifttalentforge.com',
    'www.swifttalentforge.com',
]

# Port configuration
PORT = os.getenv("PORT", "10000")

# SSL proxy settings for Render
if os.getenv("RENDER"):
    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

# Application definition
INSTALLED_APPS = [
    'Portal',
    'chat',
    'daphne',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'channels',
]

# Channels and Redis configuration
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            'hosts': [env('REDIS_URL')],
        },
    },
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Work.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'Portal' / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.static',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
            ],
        },
    },
]

ASGI_APPLICATION = "Work.asgi.application"
WSGI_APPLICATION = 'Work.wsgi.application'

# Database configuration
DATABASE_URL = env('postgres://admin:Falcon85h#@stfdb.onrender.com:5432/STFDB')
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'STFDB',
        'USER': 'ADMIN',
        'PASSWORD': 'Falcon85h#',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Localization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Kolkata'
USE_I18N = True
USE_TZ = True

# Static and media files
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Whitenoise storage configuration
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Logging configuration
LOG_DIR = BASE_DIR / 'logs'
LOG_DIR.mkdir(exist_ok=True)  # Ensure log directory exists

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
        'file': {
            'class': 'logging.FileHandler',
            'filename': LOG_DIR / 'django.log',
        },
    },
    'root': {
        'handlers': ['console', 'file'],
        'level': os.environ.get('DJANGO_LOG_LEVEL', 'WARNING'),
    },
}

# Authentication backend
AUTHENTICATION_BACKENDS = ['django.contrib.auth.backends.ModelBackend']

# Email backend
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = 'Swift Talent Forge <info@swifttalentforge.com>'

# CSRF and session security
CSRF_TRUSTED_ORIGINS = [
    'https://swifttalentforge.com',
    'https://www.swifttalentforge.com',
    'https://stf-project-0ddq.onrender.com'
]

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
