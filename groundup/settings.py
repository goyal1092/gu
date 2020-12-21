"""
Django settings for groundup project.

Generated by 'django-admin startproject' using Django 1.8.7.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

import datetime
from . import local_settings

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

try:
    BASE_DIR = local_settings.BASE_DIR
except:
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECRET KEY: This must be set in local_settings.py
SECRET_KEY = local_settings.SECRET_KEY

# DEBUG: This should be overriden in local_settings.py
try:
    DEBUG = local_settings.DEBUG
except:
    DEBUG = True

if DEBUG is False:
    ALLOWED_HOSTS = local_settings.ALLOWED_HOSTS
else:
    ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.postgres',
    'grappelli.dashboard',
    'grappelli',
    'filebrowser',
    'django.contrib.admin',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'django.contrib.sites',
    'django.contrib.humanize',
    'django.contrib.flatpages',
    'django.contrib.redirects',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    # Configure the django-otp package.
    'django_otp',
    'django_otp.plugins.otp_totp',
    'django_otp.plugins.otp_static',
    # Enable two-factor auth.
    'allauth_2fa',
    'haystack',
    'compressor',
    'ajax_select',
    'el_pagination',
    'newsroom',
    'security',
    'payment',
    'socialmedia',
    'republisher',
    'clearcache',
    'blocks',
    'letters',
    'gallery',
    'agony',
    'target',
    'sudoku',
    'analyzer',
    'pgsearch',
)

MIDDLEWARE = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',

    # Configure the django-otp package. Note this must be after the
    # AuthenticationMiddleware.
    'django_otp.middleware.OTPMiddleware',

    # Reset login flow middleware. If this middleware is included, the login
    # flow is reset if another page is loaded between login and successfully
    # entering two-factor credentials.
    'allauth_2fa.middleware.AllauthTwoFactorMiddleware',

    # SessionAuthenticationMiddleware is deprecated
    # 'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'django.contrib.redirects.middleware.RedirectFallbackMiddleware',
)

ROOT_URLCONF = 'groundup.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ os.path.join(BASE_DIR, 'templates'),],
        'APP_DIRS': True,
        'OPTIONS': {
            'debug': DEBUG,
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
                'newsroom.context_processors.newsroom_template_variables',
            ],
        },
    },
]

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)


# Set the allauth adapter to be the 2FA adapter.
ACCOUNT_ADAPTER = 'allauth_2fa.adapter.OTPAdapter'

ACCOUNT_AUTHENTICATION_METHOD = "username_email"
ACCOUNT_EMAIL_REQUIRED = True
#ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True
#ACCOUNT_EMAIL_VERIFICATION = "mandatory"
LOGIN_REDIRECT_URL = "/user/"


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'security.utils.StaffMinimumLengthValidator',
        'OPTIONS': {
            'staff_min_length': 10,
            'other_min_length': 8
        }
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]



WSGI_APPLICATION = 'groundup.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases
# This should be overriden in local_settings.py

try:
    DATABASES = local_settings.DATABASES
except:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Johannesburg'

USE_I18N = True

USE_L10N = True

USE_TZ = True

SITE_ID = 1


# CACHES: This should be overriden in local_settings.py

# NEWSROOM_CACHE_PERIOD = 600

try:
    CACHES = local_settings.CACHES
except:
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
            'LOCATION': '/var/tmp/django_cache',
            'KEY_PREFIX': 'gu',
        }
    }


STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

COMPRESS_CSS_FILTERS = [
    'compressor.filters.css_default.CssAbsoluteFilter',
    'compressor.filters.cssmin.CSSCompressorFilter'
]

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

FILEBROWSER_DIRECTORY = "uploads/"

FILEBROWSER_LIST_PER_PAGE = 150


FILEBROWSER_EXTENSIONS = {
    'Image': ['.jpg', '.jpeg', '.gif', '.png', '.tif', '.tiff'],
    'Document': ['.pdf', '.doc', '.rtf', '.txt', '.xls', '.csv'],
    'Video': ['.mov', '.wmv', '.mpeg', '.mpg', '.avi', '.rm'],
    'Audio': ['.mp3', '.mp4', '.wav', '.aiff', '.midi', '.m4p']
}

FILEBROWSER_SELECT_FORMATS = {
    'file': ['Image', 'Document', 'Video', 'Audio'],
    'image': ['Image'],
    'document': ['Document'],
    'media': ['Video', 'Audio'],
}

FILEBROWSER_VERSIONS_BASEDIR = '_versions'

FILEBROWSER_MAX_UPLOAD_SIZE = 10485760

FILEBROWSER_NORMALIZE_FILENAME = True

FILEBROWSER_CONVERT_FILENAME = True

FILEBROWSER_OVERWRITE_EXISTING = False

FILEBROWSER_VERSIONS = {
    'admin_thumbnail': {'verbose_name': 'Admin Thumbnail',
                        'width': 60, 'height': 60, 'opts': 'crop'},
    'thumbnail': {'verbose_name': 'Thumbnail',
                  'width': 60, 'height': 60, 'opts': 'crop'},
    'small': {'verbose_name': 'Small',
              'width': 140, 'height': 100, 'opts': 'crop'},
    'medium': {'verbose_name': 'Medium',
               'width': 300, 'height': '', 'opts': ''},
    'big': {'verbose_name': 'Big',
            'width': 460, 'height': '', 'opts': ''},
    'large': {'verbose_name': 'Large',
              'width': 680, 'height': '', 'opts': ''},
    'extra_large': {'verbose_name': 'Extra large',
                    'width': 750, 'height': '', 'opts': ''},
    'huge': {'verbose_name': 'Huge',
              'width': 882, 'height': '', 'opts': ''},
}

FILEBROWSER_ADMIN_VERSIONS = ['thumbnail', 'small', 'medium', 'big',
                              'large', 'extra_large', 'huge', ]

FILEBROWSER_SEARCH_TRAVERSE = True

GRAPPELLI_INDEX_DASHBOARD = 'groundup.dashboard.CustomIndexDashboard'

GRAPPELLI_ADMIN_TITLE = "GroundUp Administration"

NEWSROOM_ARTICLE_COPYRIGHT = '<p>&copy; ' + str(datetime.date.today().year) + \
                             ' GroundUp. ' \
                             'This article is licensed under a ' \
                             '<a rel="license"' \
                             '   href="http://creativecommons.org/licenses/by-nd/4.0/">' \
                             'Creative Commons Attribution-NoDerivatives 4.0 ' \
                             'International License' \
                             '</a>.</p>' \
                             '<p>You may republish this article, ' \
                             'so long as you credit the authors and ' \
                             'GroundUp, and do not change the text. ' \
                             'Please include a link back to the original ' \
                             'article.' \
                             '</p>'


NEWSROOM_SUPPORT_US_IMAGES = [
    'newsroom/images/SupportGroundUpAdvert-20180411.jpg',
]

NEWSROOM_LOGO = 'newsroom/images/Logo_white.png'

# Spam prevention
NOCAPTCHA = True

# System now uses Postgres full text search. This is Only being kept live because of the

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.simple_backend.SimpleEngine',
    },
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'file': {
            'level': 'WARNING',
            'class': 'logging.FileHandler',
            'filename': local_settings.ERROR_LOG_FILE,
            'formatter': 'verbose'
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
        }
    },
    'loggers': {
        'django': {
            'handlers': ['file', 'mail_admins', ],
            'propagate': True,
            'level': 'WARNING',
        },
        'groundup': {
            'handlers': ['file'],
            'level': 'WARNING',
            'propagate': True,
        },
    }
}

# DEPRECATED BUT CODE MUST BE REMOVED FROM VIEW FIRST
# advert_code_file_1 = open(os.path.join(BASE_DIR,
#                              "newsroom/templates/newsroom/advert_1.html"),
#                        "r")
# NEWSROOM_ADVERT_CODE_1 = advert_code_file_1.read()
# advert_code_file_2 = open(os.path.join(BASE_DIR,
#                                "newsroom/templates/newsroom/advert_2.html"),
#                        "r")
# NEWSROOM_ADVERT_CODE_2 = advert_code_file_2.read()

DONATE_PAGE = "/donate/"
#############

ACME_ADS = False
GOOGLE_ADS = False
AMAZON_ADS = False
AB_TEST_ADS = False
PIWIK_SITE_URL = ""

if AB_TEST_ADS:
    ADVERT_CODE_ACME = open(os.path.join(
        BASE_DIR, "newsroom/templates/newsroom/advert_acme.html"),
                                "r").read()
    ADVERT_CODE_GOOGLE = open(os.path.join(
        BASE_DIR, "newsroom/templates/newsroom/advert_google_responsive.html"),
                                "r").read()
    ADVERT_CODE_AMAZON = open(os.path.join(
        BASE_DIR, "newsroom/templates/newsroom/"
        "advert_amazon_gift_responsive.html"), "r").read()
elif ACME_ADS:
    NEWSROOM_ADVERT_CODE = open(os.path.join(
        BASE_DIR, "newsroom/templates/newsroom/advert_acme_responsive.html"),
                                "r").read()
elif GOOGLE_ADS:
    NEWSROOM_ADVERT_CODE = open(os.path.join(
        BASE_DIR, "newsroom/templates/newsroom/advert_google_responsive.html"),
                                "r").read()
else:
    NEWSROOM_ADVERT_CODE = ""

PIWIK_SITEID = 1
PIWIK_ENTRIES = 40

from .local_settings import *

if DEBUG is True:
    INSTALLED_APPS = INSTALLED_APPS + ('debug_toolbar',)
    MIDDLEWARE = MIDDLEWARE + \
            ('debug_toolbar.middleware.DebugToolbarMiddleware',)
