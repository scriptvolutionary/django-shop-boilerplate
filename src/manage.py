'''

    Утилита командной строки Django для административных задач.
    
'''

import os
import sys

from decouple import UndefinedValueError, config

PROJECT_NAME = 'core'

# Для разработки используйте 'settings/development.py'
# Для производства используйте 'settings/production.py'
try:
    DEV = config('DEV', cast=bool)
except UndefinedValueError:
    DEV = True

MODE = 'development' if DEV else 'production'
SETTINGS_MODULE = f'{PROJECT_NAME}.settings.{MODE}'

if __name__ == '__main__':
    '''

        Выполнение административных задач.

    '''
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', SETTINGS_MODULE)
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            'Не удалось импортировать Django. Вы уверены, что он установлен и '
            'доступен в вашей переменной окружения PYTHONPATH? Вы '
            'забыли активировать виртуальную среду?'
        ) from exc
    execute_from_command_line(sys.argv)
