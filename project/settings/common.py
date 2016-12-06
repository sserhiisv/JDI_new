# -*- coding: utf-8 -*-
# Import sys (to adjust Python path)
import sys
import os


# Import some utility functions
from os.path import abspath, basename, dirname, join, normpath

from django.utils.translation import ugettext_lazy

# #########################################################

# ##### PATH CONFIGURATION ################################

# Fetch Django's project directory
DJANGO_ROOT = dirname(dirname(abspath(__file__)))

# Fetch the project_root
PROJECT_ROOT = dirname(DJANGO_ROOT)

# The name of the whole site
SITE_NAME = basename(DJANGO_ROOT)

# Collect static files here
STATIC_ROOT = join(PROJECT_ROOT, 'run', 'static')

# Collect media files here
MEDIA_ROOT = join(PROJECT_ROOT, 'run', 'media')

# look for static assets here
STATICFILES_DIRS = [
    join(PROJECT_ROOT, 'static'),
]

# look for templates here
# This is an internal setting, used in the TEMPLATES directive
PROJECT_TEMPLATES = [
    join(PROJECT_ROOT, 'templates'),
]

# Add apps/ to the Python path
sys.path.append(normpath(join(PROJECT_ROOT, 'apps')))


# ##### APPLICATION CONFIGURATION #########################

# This are the apps
DEFAULT_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'ckeditor',
    'sorl.thumbnail',
    'hitcount',
    'compressor',
    'webapp',
]

# Middlewares
MIDDLEWARE_CLASSES = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
]

# Template stuff
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': PROJECT_TEMPLATES,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


# Context processors
'''
TEMPLATE_CONTEXT_PROCESSORS = (
  # ...
  'django.core.context_processors.request',
  # ...
)

'''

# staticfiles finder

STATICFILES_FINDERS = (
    'compressor.finders.CompressorFinder',
)

# ##### SECURITY CONFIGURATION ############################

# We store the secret key here
# The required SECRET_KEY is fetched at the end of this file
SECRET_FILE = normpath(join(PROJECT_ROOT, 'run', 'SECRET.key'))

# These persons receive error notification
ADMINS = (
    ('your name', 'your_name@example.com'),
)
MANAGERS = ADMINS


# ##### DJANGO RUNNING CONFIGURATION ######################

# The default WSGI application
WSGI_APPLICATION = '%s.wsgi.application' % SITE_NAME

# The root URL configuration
ROOT_URLCONF = '%s.urls' % SITE_NAME

# This site's ID
SITE_ID = 1

# The URL for static files
STATIC_URL = '/static/'

# The URL for media files
MEDIA_URL = '/media/'


# ##### DEBUG CONFIGURATION ###############################
DEBUG = False

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['localhost']
# ##### INTERNATIONALIZATION ##############################

LANGUAGE_CODE = 'en'
TIME_ZONE = 'Europe/Helsinki'

###
LANGUAGES = [
    ('ru', ('RU')),
    ('uk', ('UA')),
]

LOCALE_PATHS = [
    join(PROJECT_ROOT, 'locale'),
]

###

# Internationalization
USE_I18N = True

# Localisation
USE_L10N = True

# enable timezone awareness by default
USE_TZ = True


############### CKEDITOR ###########################
CKEDITOR_UPLOAD_PATH = "uploads/"


#CKEDITOR_CONFIGS = {
#    'ckeditor': {
#        'toolbar': 'none',
 #       'allowedContent': True,
 #   },
#}

CKEDITOR_CONFIGS = {
    'ckeditor': {
        'removePlugins': 'stylesheetparser',
        'toolbar': 'none',
        'allowedContent': True,
    }
}

CKEDITOR_JQUERY_URL = '//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js'
CKEDITOR_IMAGE_BACKEND = "pillow"


reload(sys)
sys.setdefaultencoding('utf8')





############################## Finally grab the SECRET KEY
try:
    SECRET_KEY = open(SECRET_FILE).read().strip()
except IOError:
    try:
        from django.utils.crypto import get_random_string
        chars = 'abcdefghijklmnopqrstuvwxyz0123456789!$%&()=+-_'
        SECRET_KEY = get_random_string(50, chars)
        with open(SECRET_FILE, 'w') as f:
            f.write(SECRET_KEY)
    except IOError:
        raise Exception('Could not open %s for writing!' % SECRET_FILE)
