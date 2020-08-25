"""
Django settings for konfetka project.

Generated by 'django-admin startproject' using Django 3.0.8.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from django.urls import reverse_lazy

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '3qn*(k_ciy-)4rob7w77_nfgh8))ok$*96fdcbs@!vbwm8dy+u'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['konfetka.com',
                 'localhost',
                 '127.0.0.1',
]

SITE_ID = 1

# Application definition
INSTALLED_APPS = [
    'account',
    'articles',
    'images',
    'actions',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'taggit',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'social_django',
    'sorl.thumbnail',
    'phonenumber_field',
    'debug_toolbar',
    "template_profiler_panel",
    'django.contrib.postgres',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

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

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'blog',
#         'USER': 'blog',
#         'PASSWORD': 'agent0071604YAR00',
#     }
# }

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Kiev'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = 'einstein16.04@gmail.com'
EMAIL_HOST_USER = 'einstein16.04@gmail.com'
EMAIL_HOST_PASSWORD = 'luspdziywpxtmkuo'
EMAIL_PORT = 25
EMAIL_USE_TLS = True

LOGIN_REDIRECT_URL = 'account:dashboard'  # куди перенаправляти користувача при успішній авторизації
LOGIN_URL = 'account:login'  # куди перенаправляти для входу в систему
LOGOUT_URL = 'account:logout'
# LOGOUT_REDIRECT_URL = 'logout'

MEDIA_URL = '/media/'  # базовий URL, від якого будуть формуватися адреси файлів
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')  # шлях у файловій системі

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'account.authentication.EmailAuthBackend',
    'social_core.backends.facebook.FacebookOAuth2',
    'social_core.backends.twitter.TwitterOAuth',
    'social_core.backends.google.GoogleOAuth2'
]

SOCIAL_AUTH_FACEBOOK_KEY = '586066032079653'  # Facebook App ID
SOCIAL_AUTH_FACEBOOK_SECRET = '211d1158a30e52e3e1e272079c985bf6'  # Facebook App Secret
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']

# Google Consumer Key
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '993446255793-uihiuvmrgm71apevv8vpks31deiobfkt.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'jM1LZMQyaZhpYua-oVKd5hUJ'  # Google Consumer Secret

PHONENUMBER_DB_FORMAT = 'INTERNATIONAL'

ABSOLUTE_URL_OVERRIDES = {
    'auth.user': lambda u: reverse_lazy('account:user_detail', args=[u.username])
}

# THUMBNAIL_DEBUG = True
REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_DB = 0

INTERNAL_IPS = [
    '127.0.0.1',
]

DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
    'debug_toolbar.panels.profiling.ProfilingPanel',
    "template_profiler_panel.panels.template.TemplateProfilerPanel",
]