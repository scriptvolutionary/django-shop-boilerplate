'''

    Настройки Django для разработки.
    
'''

from decouple import UndefinedValueError, config

from core.settings.base import *

# ПРЕДУПРЕЖДЕНИЕ О БЕЗОПАСНОСТИ: не запускайте программу с включенной отладкой!
# Если DEBUG не установлен в разработке, будет True.
try:
    DEBUG = config('DEBUG', cast=bool)
except UndefinedValueError:
    DEBUG = True

# Включая '127.0.0.1' для debug_toolbar
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

# INSTALLED_APPS = {} объявлено в base.py
INSTALLED_APPS += [
    'django_browser_reload',
    'debug_toolbar',
]

# MIDDLEWARE = {} объявлено в base.py
MIDDLEWARE += [
    "django_browser_reload.middleware.BrowserReloadMiddleware",
    # Для панели инструментов debug_toolbar
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

# Настройки панели откладки

DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
]


# Показать или скрыть панель инструментов debug_toolbar
def show_toolbar(request):
    return DEBUG


DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
    'SHOW_TOOLBAR_CALLBACK': show_toolbar,
}

# DATABASES = {} объявлено в base.py
DATABASES['default'] = {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': BASE_DIR / 'db.sqlite3',
}

# STRIPE_PUBLIC_KEY = config('STRIPE_TEST_PUBLIC_KEY')
# STRIPE_SECRET_KEY = config('STRIPE_TEST_SECRET_KEY')
