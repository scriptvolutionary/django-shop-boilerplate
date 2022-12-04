'''

	Конфигурация WSGI для этого проекта.

	Он предоставляет вызываемый WSGI как переменную уровня модуля с именем ``application``.

	Дополнительные сведения об этом файле см.
	https://docs.djangoproject.com/ru/3.1/howto/deployment/wsgi/

	В производстве этот используемый файл используется для запуска приложения.
	Мы выбираем SETTINGS_MODULE, который определен в manage.py.

'''

import os

from django.core.wsgi import get_wsgi_application

from manage import SETTINGS_MODULE

os.environ.setdefault('DJANGO_SETTINGS_MODULE', SETTINGS_MODULE)
application = get_wsgi_application()
