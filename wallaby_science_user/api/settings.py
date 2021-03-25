"""
Django settings for api project.

Generated by 'django-admin startproject' using Django 3.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'yz+@(y^2j6-r$iqxxgh^optx#$76g!ur_qs07l$f^)=4c*v#24'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DEBUG', False)

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'detection',
    'run',
    'instance',
    'products',
    'sources',
    'tag',
    'comments',
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

ROOT_URLCONF = 'api.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'api.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

# Optional database environment variables (default postgresql)
DJANGO_DATABASE_ENGINE = os.getenv('DJANGO_DATABASE_ENGINE', 'django.db.backends.postgresql')
DJANGO_DATABASE_HOST = os.getenv('DJANGO_DATABASE_HOST', '127.0.0.1')
DJANGO_DATABASE_PORT = os.getenv('DJANGO_DATABASE_PORT', '5432')

# Required database environment variables
DJANGO_DATABASE_NAME = os.environ['DJANGO_DATABASE_NAME']
DJANGO_DATABASE_USER = os.environ['DJANGO_DATABASE_USER']
DJANGO_DATABASE_PASSWORD = os.environ['DJANGO_DATABASE_PASSWORD']

DATABASES = {
    'default': {
        'ENGINE': DJANGO_DATABASE_ENGINE,
        'OPTIONS': {
            'options': '-c search_path=public,wallaby'
        },
        'NAME': DJANGO_DATABASE_NAME,
        'USER': DJANGO_DATABASE_USER,
        'PASSWORD': DJANGO_DATABASE_PASSWORD,
        'HOST': DJANGO_DATABASE_HOST,
        'PORT': DJANGO_DATABASE_PORT,
    },
    'wallaby': {
        'ENGINE': DJANGO_DATABASE_ENGINE,
        'OPTIONS': {
            'options': '-c search_path=wallaby'
        },
        'NAME': DJANGO_DATABASE_NAME,
        'USER': DJANGO_DATABASE_USER,
        'PASSWORD': DJANGO_DATABASE_PASSWORD,
        'HOST': DJANGO_DATABASE_HOST,
        'PORT': DJANGO_DATABASE_PORT,
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'


# Notebook settings
NOTEBOOK_ARGUMENTS = [
    '--allow-root',
    '--no-browser', 
]