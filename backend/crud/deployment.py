import os
from pathlib import Path
from settings import BASE_DIR



# SECURITY WARNING: keep the secret key used in production secret!
# In production, this should be set as an environment variable


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DJANGO_DEBUG', '') != 'False'

ALLOWED_HOSTS = [os.environ['WEBSITE_HOSTNAME']] 
CSRF_TRUSTED_ORIGINS = ['https://' + os.environ['WEBSITE_HOSTNAME']] 
DEBUG = False
SECRET_KEY = os.environ['MY_SECRET_KEY']

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Add whitenoise middleware
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

STORAGES = {
    'default': {
        'BACKEND': 'django.core.files.storage.FileSystemStorage',
    },
    'static': {
        'BACKEND': 'whitenoise.storage.CompressedStaticFilesStorage',
    },
}



WSGI_APPLICATION = 'backend.wsgi.application'


CONNECTION = os.environ.get('AZURE_STORAGE_CONNECTIONSTRING')
CONNECTION_STR = {pair.split('=')[0]: pair.split('=')[1] for pair in CONNECTION.split(';')}
# Database
# Use Azure PostgreSQL in production
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': CONNECTION_STR['dbname'],
        'USER': CONNECTION_STR['user'],
        'PASSWORD': CONNECTION_STR['password'],
        'HOST': CONNECTION_STR['host'],
        'OPTIONS': {'sslmode': 'require'},
    }
}

# CORS settings
# CORS_ALLOWED_ORIGINS = [
#     ''
# ]


# Password validation
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


STATIC_URL = '/static/'  # The URL to use when referring to static files
STATIC_ROOT = BASE_DIR/'staticfiles'


# Sentence transformer path - Consider using Azure Blob Storage for production
# LOCAL_SENTENCE_TRANSFORMER_PATH = os.environ.get('SENTENCE_TRANSFORMER_PATH', r'C:\Users\TapasmitaPattanaik\Desktop\ReactClone\backend')
