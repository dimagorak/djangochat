"""
Django settings for djangochat project.

Generated by 'django-admin startproject' using Django 1.11.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
from datetime import timedelta
import django_heroku
import dj_database_url
from urllib.parse import urlparse
import redis

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'b9r!y7loml1zcr7pw+ounb12g%yb(!pi8bha9q-&#4yw2yw$uc'
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'b9r!y7loml1zcr7pw+ounb12g%yb(!pi8bha9q-&#4yw2yw$uc')
# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True
DEBUG = bool(os.environ.get('DJANGO_DEBUG', True))

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'chatdemo.apps.ChatdemoConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'widget_tweaks',
    'channels',
    'channels_presence',
    'celery',
    'django_celery_beat',
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

ROOT_URLCONF = 'djangochat.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'djangochat.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd5a5cbbt4qiqsk',
        'USER': 'qvpojhochtlvoz',
        'PASSWORD': 'c60e18a6870300911a97200c3023c0f386b1a012a122b027f1f30e1f6bc9791e',
        'HOST': 'ec2-54-235-169-191.compute-1.amazonaws.com',
        'PORT': 5432,
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

dj_from_env = dj_database_url.config()
DATABASES['default'].update(dj_from_env)

LOGIN_URL = '/login/'

LOGIN_REDIRECT_URL = '/'

EMAIL_BACKEND = 'postmarker.django.EmailBackend'
POSTMARK = {
    'TOKEN': '|c8|ump-]d}6Q°@uqiJ%]{ahzUHlE8s)>,rrx+FVeLt?l§T_gBoE.i!4oqdLq:a[',
    'TEST_MODE': False,
}

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "redis_cache.RedisCache",
        "CONFIG": {
            "hosts": [os.environ.get('REDIS_URL', '9219')],
        },
        "ROUTING": "chatdemo.routing.channel_routing",
    },
}
# redis_url = urlparse(os.environ.get('REDISTOGO_URL', 'redis://localhost:9219'))
#
# CACHES = {
#     'default': {
#         'BACKEND': 'redis_cache.RedisCache',
#         'LOCATION': '%s:%s' % (redis_url.hostname, redis_url.port),
#         'OPTIONS': {
#             'DB': 1,
#             'PASSWORD': redis_url.password,
#         }
#     }
# }
# r = redis.from_url(os.environ.get("REDIS_URL"))
# CACHES = {
#     "default": {
#          "BACKEND": "redis_cache.RedisCache",
#          "LOCATION": os.environ.get('REDIS_URL'),
#     }
# }
django_heroku.settings(locals())
