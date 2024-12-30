import os
from .settings import *
from .settings import BASE_DIR

ALLOWED_HOSTS = [os.environ['WEBSITE_HOSTNAME']] 
CSRF_TRUSTED_ORIGINS = ['https://'+os.environ['WEBSITE_HOSTNAME']]
DEBUG = False

SECRET_KEY = os.environ['MY_SECRET_KEY']

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware', 
    'whitenoise.middleware.WhiteNoiseMiddleware', # Add CORS middleware early
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# CORS_ALLOWED_ORIGINS = [

# ]

STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },  
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

CONNECTION = os.environ['AZURE_POSTGRESQL_CONNECTION_STRING']
CONNECTION_STR = {pairs.split('=')[0]:pairs.split('=')[1] for pairs in CONNECTION.split(';')}
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': CONNECTION_STR['dbname'],
        'USER': CONNECTION_STR['user'],
        'PASSWORD': CONNECTION_STR['password'],
        'HOST' : CONNECTION_STR['host'],
    }
}

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')