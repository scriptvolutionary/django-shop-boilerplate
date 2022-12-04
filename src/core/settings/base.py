'''

    Настройки Django для этого проекта.

    Дополнительные сведения об этом файле см.
    https://docs.djangoproject.com/ru/3.1/topics/settings/

    Полный список настроек и их значений см.
    https://docs.djangoproject.com/ru/3.1/ref/settings/
    
'''

from pathlib import Path

from decouple import config

from app.vars import NAME as MAIN_APP
from manage import PROJECT_NAME

# Создайте пути внутри проекта следующим образом: BASE_DIR / 'subdir'.
# Настроил BASE_DIR, изменив settings.py на каталог настроек.
# Этим мы выбираем src как BASE_DIR.
# Текущее имя файла — base.py. Родителем base.py являются настройки.
# настройки -> родитель -> <каталог> -> родитель -> src.
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent.parent

# TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')
TEMPLATE_DIR = BASE_DIR / 'templates'


# Настройки быстрого старта разработки - непригодны для продакшена
# См. https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# ПРЕДУПРЕЖДЕНИЕ О БЕЗОПАСНОСТИ: держите секретный ключ, используемый в производстве, в секрете!
# Получение SECRET_KEY с развязкой
SECRET_KEY = config('SECRET_KEY')


# Определение приложения

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    MAIN_APP,
]

MIDDLEWARE = [
    # Часть базы
    'django.middleware.security.SecurityMiddleware',
    # Из WhiteNoise для обслуживания статических файлов в Heroku из Django
    # Удалите это, если вы используете S3
    'whitenoise.middleware.WhiteNoiseMiddleware',
    # Часть базы
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = f'{PROJECT_NAME}.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],
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

WSGI_APPLICATION = f'{PROJECT_NAME}.wsgi.application'

# База данных
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
DATABASES = {}

# Проверка пароля
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},  # noqa: E501
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},  # noqa: E501
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},  # noqa: E501
]


# Интернационализация
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'ru-ru'
TIME_ZONE = 'Europe/Moscow'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Статические файлы (CSS, JavaScript, Изображения)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_ROOT = BASE_DIR / 'public'
STATIC_URL = '/static/'

# Храните ваши статические файлы здесь.
# collectstatic будет использовать этот каталог для создания статических файлов в STATIC_ROOT.
STATICFILES_DIRS = [BASE_DIR / 'static']

# Медиафайлы (загруженные пользователями)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
