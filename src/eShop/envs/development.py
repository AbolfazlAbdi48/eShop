from .common import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'eshop_db',
        'USER': 'eshop_user',
        'PASSWORD': '123456Ab',
        'HOST': 'db',
        'PORT': 5432,
    }
}
