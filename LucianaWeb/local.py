from .settings import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'lupagina',
        'USER' : 'root',
        'PASSWORD': 'root',
        'HOST' : 'localhost',
        'PORT' : '3306',
    }
}


import django_heroku
django_heroku.settings(locals())