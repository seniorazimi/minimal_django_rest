from pathlib import Path
from datetime import timedelta
from rest_framework.settings import api_settings

# Security Options
SECRET_KEY = 'django-insecure-h_7m2!x$&=&(1$1m^!-)yekgamvn0f5cig2$5zh=g#$42kgery'
DEBUG = True
ALLOWED_HOSTS = ['*']

# Application definition
INSTALLED_APPS = [
    'minimal_django_rest',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'rest_framework',  # to install rest_framework
    'knox'  # to install knox
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'minimal_django_rest.urls'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': './db.sqlite3',
    }
}

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# pk type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# knox settings
REST_KNOX = {
    'SECURE_HASH_ALGORITHM': 'cryptography.hazmat.primitives.hashes.SHA512',  # hashing algorithm for token storage
    'TOKEN_TTL': timedelta(hours=10),  # expire time
    'USER_SERIALIZER': 'knox.serializers.UserSerializer',
    'AUTO_REFRESH': True,  # reset expire timer each time the token is used
}

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': ('knox.auth.TokenAuthentication',),  # set default
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ]
}
