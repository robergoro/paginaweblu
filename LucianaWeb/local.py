from .settings import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'robergoro1',
        'USER' : 'robergoro1',
        'PASSWORD': 'robergoro1',
        'HOST' : 'localhost',
        'PORT' : '3306',
    }
}
