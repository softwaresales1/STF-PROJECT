import os  
PORT = os.getenv("PORT", "10000")
from urllib.parse import urlparse
import environ
import dj_database_url

# Initialize environment variables using django-environ
env = environ.Env(
    DEBUG=(bool, False),
    DJANGO_SECRET_KEY=(str, 'fallback-secret-key'),
    DB_NAME=(str, 'your-db-name'),
    DB_USER=(str, 'your-db-user'),
    DB_PASSWORD=(str, 'your-db-password'),
    DB_HOST=(str, 'localhost'),
    DB_PORT=(str, '5432'),
    REDIS_URL=(str, 'redis://localhost:6379/0'),
    EMAIL_HOST_USER=(str, 'your-email@gmail.com'),
    EMAIL_HOST_PASSWORD=(str, 'your-email-password'),
)
environ.Env.read_env()  # Reading .env file for local development

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('DJANGO_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool('DEBUG', default=False)

# ALLOWED_HOSTS now includes Render hostname, your custom domains, and Render's static outbound IPs
ALLOWED_HOSTS = [
    'stf-trial.onrender.com',      # Render hostname
    '127.0.0.1',                   # Localhost
    'swifttalentforge.com',        # Custom domain
    'www.swifttalentforge.com',    # Custom domain with www
    '100.20.92.101',               # Render static outbound IP
    '44.225.181.72',               # Render static outbound IP
    '44.227.217.144',              # Render static outbound IP
]

# Optional: If using django-cors-headers for API requests, enable CORS
# Uncomment the following lines if needed.
# INSTALLED_APPS += ['corsheaders']
# MIDDLEWARE.insert(0, 'corsheaders.middleware.CorsMiddleware')
# CORS_ALLOWED_ORIGINS = [
#     'https://stf-trial.onrender.com',
#     'https://swifttalentforge.com',
#     'https://www.swifttalentforge.com',
#     'http://100.20.92.101',
#     'http://44.225.181.72',
#     'http://44.227.217.144',
# ]

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

# Configure Channels to use Redis as the channel layer
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
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Static files handling in production
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
        'DIRS': [os.path.join(BASE_DIR, 'Portal/templates')],
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

# Parse the DATABASE_URL environment variable
DATABASE_URL = os.getenv('DATABASE_URL')

if DATABASE_URL:
    DATABASES = {
        'default': dj_database_url.config(default=DATABASE_URL, conn_max_age=600, ssl_require=True)
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': env('DB_NAME'),
            'USER': env('DB_USER'),
            'PASSWORD': env('DB_PASSWORD'),
            'HOST': env('DB_HOST'),
            'PORT': env('DB_PORT'),
        }
    }

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Localization settings
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Kolkata'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),  # Directory for static files during development
]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  # Directory for collected static files in production

# Whitenoise storage configuration
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Logging configuration
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
        'file': {
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/django.log'),
        },
    },
    'root': {
        'handlers': ['console', 'file'],
        'level': os.environ.get('DJANGO_LOG_LEVEL', 'WARNING'),
    },
}

# Authentication backend
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
]

# Email backend configuration
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = 'Swift Talent Forge <info@swifttalentforge.com>'

# CSRF and Session security
CSRF_TRUSTED_ORIGINS = [
    'https://swifttalentforge.com',
    'https://www.swifttalentforge.com',
    'https://stf-trial.onrender.com'
]

SESSION_COOKIE_SECURE = True  # Ensures session cookies are only sent over HTTPS
CSRF_COOKIE_SECURE = True     # Ensures CSRF cookies are only sent over HTTPS