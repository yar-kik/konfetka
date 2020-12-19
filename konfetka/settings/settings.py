"""
Django settings for konfetka project.

Generated by 'django-admin startproject' using Django 3.0.8.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import environ
from django.urls import reverse_lazy

env = environ.Env(
    DEBUG=(bool, False)
)
environ.Env.read_env()
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


SECRET_KEY = env('SECRET_KEY')

SITE_ID = 1

ROOT_URLCONF = 'konfetka.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

WSGI_APPLICATION = 'konfetka.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env("DATABASE_NAME"),
        'USER': env("DATABASE_USER"),
        'PASSWORD': env("DATABASE_PASSWORD"),
        'CONN_MAX_AGE': 60,
    }
}

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'uk-ua'
TIME_ZONE = 'Europe/Kiev'
USE_I18N = True
USE_L10N = True
USE_TZ = False

STATIC_URL = '/static/'

MEDIA_URL = '/media/'  # базовий URL, від якого будуть формуватися адреси файлів
MEDIA_ROOT = os.path.join(BASE_DIR, '../media/')  # шлях у файловій системі

MAX_UPLOAD_IMAGE_SIZE = 2097152  # equal 2Mb
VALID_IMAGE_EXTENSION = ['jpg', 'jpeg', 'png']

CKEDITOR_BASEPATH = "/static/ckeditor/ckeditor/"
CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_CONFIGS = {
    'default': {
         'toolbar': [
            ['Undo', 'Redo',
             '-', 'Bold', 'Italic', 'Underline', 'Strike', "Subscript", "Superscript",
             '-', "RemoveFormat",
             '-', 'NumberedList', 'BulletedList',
             '-', 'Outdent', 'Indent',
             '-', 'Blockquote',
             '-', 'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock',
            ],
            ['Image',
             '-', 'HorizontalRule',
             '-', 'Link', 'Unlink',
             '-', 'Format', "Styles", "FontSize",
             '-', "TextColor",
             '-', 'Maximize',
            ]
        ],
        'height': 600,
        'width': '100%',
    },
}


LOGIN_REDIRECT_URL = 'account:dashboard'  # куди перенаправляти користувача при успішній авторизації
LOGIN_URL = 'account:login'  # куди перенаправляти для входу в систему
LOGOUT_URL = 'account:logout'
# LOGOUT_REDIRECT_URL = 'logout'

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'account.authentication.EmailAuthBackend',
    'account.authentication.PhoneAuthBackend',
    'social_core.backends.facebook.FacebookOAuth2',
    'social_core.backends.twitter.TwitterOAuth',
    'social_core.backends.google.GoogleOAuth2'
]

SOCIAL_AUTH_FACEBOOK_KEY = env('FACEBOOK_KEY')  # Facebook App ID
SOCIAL_AUTH_FACEBOOK_SECRET = env('FACEBOOK_SECRET')  # Facebook App Secret
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = env('GOOGLE_OAUTH2_KEY')
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = env('GOOGLE_OAUTH2_SECRET')  # Google Consumer Secret

ADMINS = [("Yaroslav", "einstein16.04@gmail.com"),
          ("Sveta", "misstkachuk15@gmail.com")]

EMAIL_HOST = env('EMAIL_HOST')
EMAIL_HOST_USER = env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
EMAIL_PORT = env("EMAIL_PORT")
EMAIL_USE_SSL = True

PHONENUMBER_DB_FORMAT = 'NATIONAL'
PHONENUMBER_DEFAULT_REGION = 'UA'

ABSOLUTE_URL_OVERRIDES = {
    'auth.user': lambda u: reverse_lazy('account:user_detail', args=[u.username])
}

REDIS_HOST = env('REDIS_HOST')
REDIS_PORT = env("REDIS_PORT")
REDIS_DB = 0

INTERNAL_IPS = [
    '127.0.0.1',
]


CACHES = {
    "default": {
        "BACKEND": "redis_cache.RedisCache",
        "LOCATION": 'localhost:6379',
        "OPTIONS": {
            "DB": 1,
        }
    }
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} [{asctime}] "{message}", {name} {filename} line {lineno}, in {funcName}',
            'datefmt': "%Y-%m-%d %H:%M:%S",
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
        'mail_admins': {
            'level': 'ERROR',
            'formatter': 'verbose',
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': True,
        },
        "file": {
            'level': "WARNING",
            'formatter': "verbose",
            'class': "logging.FileHandler",
            'filename': "warnings.log",
        },
    },
    'loggers': {
        '': {
            'level': 'INFO',
            'handlers': ['console', 'file', 'mail_admins'],
            'propagate': True,
        },
        'django.request': {
            'handlers': ['file', 'mail_admins'],
            'level': 'WARNING',
            "propagate": False,
        },
        'django.security': {
            'handlers': ['file', 'mail_admins'],
            'level': 'WARNING',
            "propagate": False,
        },
    }
}
