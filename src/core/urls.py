'''

    Пример конфигурации URL

    Список `urlpatterns` направляет URL-адреса в представления. Для получения дополнительной информации см.:
        https://docs.djangoproject.com/ru/3.1/topics/http/urls/
        
    Примеры:
    Представления функций
        1. Добавьте импорт: из представлений импорта my_app
        2. Добавьте URL-адрес в urlpatterns: path('', views.home, name='home')
    Представления на основе классов
        1. Добавьте импорт: from other_app.views import Home
        2. Добавьте URL-адрес в шаблоны URL-адресов: path('', Home.as_view(), name='home')
    Включение другой конфигурации URL
        1. Импортируйте функцию include(): из django.urls import include, path
        2. Добавьте URL-адрес в urlpatterns: path('blog/', include('blog.urls'))
        
'''

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from app.vars import NAME as MAIN_APP

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(f'{MAIN_APP}.urls', namespace=MAIN_APP)),
    path("__reload__/", include("django_browser_reload.urls")),
]

if settings.DEBUG:
    import debug_toolbar

    # Для панели инструментов отладки Django в режиме отладки.
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]

    # Для обслуживания статических файлов в режиме отладки
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)

    # Для обслуживания медиафайлов в режиме отладки
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
