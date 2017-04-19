"""
Django settings for openstack_lease_it project.

Generated by 'django-admin startproject' using Django 1.8.7.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from config import load_config

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

GLOBAL_CONFIG = load_config()

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = GLOBAL_CONFIG['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = GLOBAL_CONFIG['DEBUG']

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'openstack_auth',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'openstack_lease_it',
    'lease_it',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'openstack_lease_it.urls'

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

WSGI_APPLICATION = 'openstack_lease_it.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en'

TIME_ZONE = 'Europe/Paris'

USE_I18N = True

USE_L10N = True

USE_TZ = True
DEFAULT_CHARSET = 'utf-8'

SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '{MEMCACHED_HOST}:{MEMCACHED_PORT}'.format(**GLOBAL_CONFIG),
    }
}
SESSION_COOKIE_SECURE = False
SESSION_TIMEOUT = 1800
# A token can be near the end of validity when a page starts loading, and
# invalid during the rendering which can cause errors when a page load.
# TOKEN_TIMEOUT_MARGIN defines a time in seconds we retrieve from token
# validity to avoid this issue. You can adjust this time depending on the
# performance of the infrastructure.
TOKEN_TIMEOUT_MARGIN = 100

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

LOGIN_URL = 'login'
LOGOUT_URL = 'logout'
LOGIN_REDIRECT_URL = '/'

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.PickleSerializer'

if GLOBAL_CONFIG['BACKEND_PLUGIN'] == 'Openstack':
    # UserId on django-openstack_auth need specific User model
    AUTH_USER_MODEL = 'openstack_auth.User'

    # Define keystone URL for authentification
    OPENSTACK_KEYSTONE_URL = GLOBAL_CONFIG['OS_AUTH_URL']

    # We use keystone v3 API
    OPENSTACK_API_VERSIONS = {
        "identity": GLOBAL_CONFIG['OS_IDENTITY_API_VERSION'],
    }
    # We use multidomain
    OPENSTACK_KEYSTONE_MULTIDOMAIN_SUPPORT = True

    # We load Openstack_auth backend
    AUTHENTICATION_BACKENDS = (
        'openstack_auth.backend.KeystoneBackend',
        'django.contrib.auth.backends.ModelBackend',
    )
else:
    AUTHENTICATION_BACKENDS = (
        'django.contrib.auth.backends.ModelBackend',
    )
