"""
Django settings for hxmirador project.

Generated by 'django-admin startproject' using Django 2.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
SETTINGS_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(SETTINGS_DIR)
PROJECT_NAME = "hxmirador"

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("HXMIRADOR_DJANGO_SECRET_KEY", "CHANGE_ME")

# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["localhost", "127.0.0.1"]
allowed_hosts_other = os.environ.get("HXMIRADOR_ALLOWED_HOSTS", "")
if allowed_hosts_other:
    ALLOWED_HOSTS.extend(allowed_hosts_other.split())


# Application definition
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "hxlti",
    "mirador",
    "corsheaders",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
]

ROOT_URLCONF = PROJECT_NAME + ".urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = PROJECT_NAME + ".wsgi.application"


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases
HXMIRADOR_DB_PATH = os.environ.get(
    "HXMIRADOR_DB_PATH", os.path.join(BASE_DIR, PROJECT_NAME + "_sqlite3.db")
)
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": HXMIRADOR_DB_PATH,
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    #    {
    #        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    #    },
    #    {
    #        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    #    },
    #    {
    #        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    #    },
    #    {
    #        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    #    },
]


# Logging config
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "simple": {
            "format": (
                "%(asctime)s|%(levelname)s [%(filename)s:%(funcName)s]" " %(message)s"
            )
        },
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "simple",
            "stream": "ext://sys.stdout",
        },
        "errorfile_handler": {
            "level": "DEBUG",
            "class": "logging.handlers.RotatingFileHandler",
            "formatter": "simple",
            "filename": os.path.join(BASE_DIR, PROJECT_NAME + "_errors.log"),
            "maxBytes": 10485760,  # 10MB
            "backupCount": 7,
            "encoding": "utf8",
        },
    },
    "loggers": {
        "mirador": {"level": "DEBUG", "handlers": ["console"], "propagate": True},
        "hxlti_dj": {"level": "DEBUG", "handlers": ["console"], "propagate": True},
        "oauthlib": {
            "level": "DEBUG",
            "handlers": ["console"],
            "propagate": True,
        },
        "root": {
            "level": "DEBUG",
            "handlers": ["console"],
        },
    },
}


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/
LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/
STATIC_URL = "/static/"
STATIC_ROOT = os.environ.get("HXMIRADOR_STATIC_ROOT", os.path.join(BASE_DIR, "static/"))

# hxlti app settings
# assuming ssl terminator in front of django (nginx reverse proxy)
use_ssl = os.environ.get("HXLTI_ENFORCE_SSL", "false")
HXLTI_ENFORCE_SSL = use_ssl.lower() == "true"
HXLTI_DUMMY_CONSUMER_KEY = os.environ.get(
    "HXLTI_DUMMY_CONSUMER_KEY",
    "dummy_42237E2AB9614C4EAB0C089A96B40686B1C97DE114EC40659E64F1CE3C195AAC",
)
HXLTI_REDIS_URL = os.environ.get("REDIS_URL", "redis://localhost:6379/0")

#
# settings for django-cors-headers
#
CORS_ORIGIN_ALLOW_ALL = True  # accept requests from anyone


# hxmirador lti params mapping
HXMIRADOR_CUSTOM_PARAMETERS_MAP = {
    "custom_canvas_ids": {
        "ptype": "list",
        "mapto": "canvases",
    },
    "custom_object_ids": {
        "ptype": "list",
        "mapto": "manifests",
    },
    "custom_layout": {
        "ptype": "string",
        "mapto": "layout",
    },
    "custom_view_type": {
        "ptype": "string",
        "mapto": "view_type",
    },
    # if there's multiple params that map to the same var name
    # and the request sends these multiple params (say with different values)
    # the last one defined in this MAP takes precedence.
    "custom_manifests": {
        "ptype": "list",
        "mapto": "manifests",
    },
}
