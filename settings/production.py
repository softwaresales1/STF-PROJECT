# Production settings for the Django project

import os

# Define BASE_DIR
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Basic settings
DEBUG = False
ALLOWED_HOSTS = ['yourdomain.com']

# Database settings
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME', 'your_db_name'),  # Replace with actual database name
        'USER': os.getenv('DB_USER', 'your_db_user'),  # Replace with actual database user
        'PASSWORD': os.getenv('DB_PASSWORD', 'your_db_password'),  # Replace with actual password
        'HOST': os.getenv('DB_HOST', 'localhost'),
        'PORT': os.getenv('DB_PORT', '5432'),
    }
}

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Other production settings can be added here
