import os
from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'todo.settings')

# Создаем объект приложения Celery, используя имя модуля 'todo'
# и используем предварительно настроенные настройки из Django
app = Celery('todo')

# Загружаем модули задач из всех зарегистрированных приложений Django.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Автоматическое обнаружение задач в приложениях Django
app.autodiscover_tasks()
