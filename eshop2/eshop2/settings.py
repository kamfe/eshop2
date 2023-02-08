"""
Generated by 'django-admin startproject' using Django 4.1.5
"""
from os import environ, path
from pathlib import Path
from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())

BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = environ.get('SECRET_KEY')

DEBUG = environ.get('DEBUG')

ALLOWED_HOSTS = []


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sites',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'users',
    'products',
    'cart',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.github',
    'django_cleanup.apps.CleanupConfig',
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

ROOT_URLCONF = 'eshop2.urls'

AUTH_USER_MODEL = 'users.MyUser'

# allauth
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

SITE_ID = int(environ.get('SITE_ID'))

ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'

ACCOUNT_FORMS = {
    'login': 'users.forms.CustomLoginForm',
    'signup': 'users.forms.CustomSignupForm',
}
# allauth end

# smtp
EMAIL_BACKEND = environ.get('ESHOP_EMAIL_BACKEND')
EMAIL_HOST = environ.get('ESHOP_EMAIL_HOST')
EMAIL_HOST_USER = environ.get('ESHOP_EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = environ.get('ESHOP_EMAIL_HOST_PASSWORD')
EMAIL_PORT = environ.get('ESHOP_EMAIL_PORT')
EMAIL_USE_TLS = environ.get('ESHOP_EMAIL_USE_TLS')

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'cart.context_processors.cart'
            ],
        },
    },
]

WSGI_APPLICATION = 'eshop2.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': environ.get('ESHOP_DATABASE_ENGINE'),
        'NAME': environ.get('ESHOP_DATABASE_NAME'),
        'USER': environ.get('ESHOP_DATABASE_USER'),
        'PASSWORD': environ.get('ESHOP_DATABASE_PASSWORD'),
        'HOST': environ.get('ESHOP_DATABASE_HOST'),
        'PORT': environ.get('ESHOP_DATABASE_PORT')
    }
}

LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATICFILES_DIRS = [
    BASE_DIR / "static",
]

STATIC_URL = '/static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MEDIA_URL = "/media/"
MEDIA_ROOT = path.join(BASE_DIR, 'media')

CART_SESSION_ID = 'cart'
