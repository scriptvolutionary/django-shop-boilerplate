'''

	Конфигурация ASGI для этого проекта.

	Он предоставляет вызываемый ASGI как переменную уровня модуля с именем «приложение».

	Дополнительные сведения об этом файле см.
	https://docs.djangoproject.com/ru/3.1/howto/deployment/asgi/

'''

import os

from django.core.asgi import get_asgi_application

from manage import SETTINGS_MODULE

os.environ.setdefault('DJANGO_SETTINGS_MODULE', SETTINGS_MODULE)
application = get_asgi_application()
