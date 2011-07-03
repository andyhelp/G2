# Django settings for pydj project.

import os
import sys

PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, os.path.join(PROJECT_PATH, "apps/"))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

# Required when used with fastcgi
FORCE_SCRIPT_NAME = ''

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': os.path.join(PROJECT_PATH, 'pydj'),                      # Or path to database file if using sqlite3.
        'USER': 'pydj',                      # Not used with sqlite3.
        'PASSWORD': 'pydj',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = ''

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'x1da5l)w(+*0_&u&qw!2u@ivj+s3wluc($d(9%#=w5m6a+p=4a'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'pydj.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    'pydj.playlist',
    'forum',
    'django.contrib.markup',
    'django_extensions',
    'rss_upload',
)


AUTH_PROFILE_MODULE = "playlist.UserProfile"
#    Set this to "playlist.UserProfile"

LOGIN_REDIRECT_URL = "/playlist"
LOGIN_URL = "/login"
TEMPLATE_CONTEXT_PROCESSORS = (
        "django.contrib.auth.context_processors.auth",
        "django.core.context_processors.debug",
        "django.core.context_processors.i18n",
        "django.core.context_processors.media",
        "django.contrib.messages.context_processors.messages",
        'playlist.context.listenersContextProcessor',
        'playlist.context.newReportsContextProcessor',
        'playlist.context.newEditsContextProcessor',
        'playlist.context.positionContextProcessor',
        'playlist.context.commentProcessor',
        'playlist.context.nowPlayingContextProcessor',
        'playlist.context.SQLLogContextProcessor',
        'playlist.context.siteContext',
        ) 
    
IMAGES_DIR = os.path.join(PROJECT_PATH, 'playlist/images') 

LOGIC_DIR = os.path.join(PROJECT_PATH, 'playlist/logic')

SHOW_QUERIES = False

ICES_CONF = os.path.join(PROJECT_PATH, 'playlist/logic/ices.conf')

STREAMINFO_URL='http://'
STREAMINFO_MOUNT_POINT = ''

NEXT_PASSWORD = 'nextp'

MAX_UPLOAD_SIZE = 15000000 #15MB

MAX_SONG_LENGTH = 10 * 60 #10 minutes

PLAYLIST_MAX = 100

PLAYLIST_SOFT_TIME_LIMIT = 3 * 60	#3 hours

REPLAY_INTERVAL = 1

IS_LIVE = False

FILE_UPLOAD_MAX_MEMORY_SIZE = 0

SITE_TITLE = 'Set Title!'

LISTEN_URL = 'http://'

DEAD_AIR_TRACK = os.path.join(PROJECT_PATH, 'playlist/logic/bees.mp3')

REGISTER_SA_VERIFICATION = False

