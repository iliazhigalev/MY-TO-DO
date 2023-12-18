from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Установка переменной окружения, чтобы использовать файл настроек Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'todo.settings')

# Создание экземпляра Celery и назначение его конфигурации из Django settings
app = Celery('todo')
app.config_from_object('django.conf:settings', namespace='CELERY')

# Загрузка задач из всех зарегистрированных приложений Django
app.autodiscover_tasks()
