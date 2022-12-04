'''

    Настройки Django для деплоя.
    
'''

import dj_database_url
from decouple import config

from core.settings.base import *

# Включите сюда свои хосты
ALLOWED_HOSTS = ['*']

# Перенаправление не-ssl-запросов на ssl-версию.
SECURE_SSL_REDIRECT = True

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': config('DB_NAME'),
#         'USER': config('DB_USER'),
#         'PASSWORD': config('DB_PASSWORD'),
#         'HOST': config('DB_HOST'),
#         'PORT': ''
#     }
# }

# Создание БД директории с dj_database_url из DATABASE_URL
postgres_db = dj_database_url.parse(config('DATABASE_URL'), conn_max_age=600)

# DATABASES = {} объявлено в base.py
DATABASES['default'] = postgres_db

# STRIPE_PUBLIC_KEY = config('STRIPE_LIVE_PUBLIC_KEY')
# STRIPE_SECRET_KEY = config('STRIPE_LIVE_SECRET_KEY')
