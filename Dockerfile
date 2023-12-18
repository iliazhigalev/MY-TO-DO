FROM python:3.10

# Установите переменную окружения для предотвращения буферизации вывода Python
ENV PYTHONUNBUFFERED 1

# Устанавливаем переменную окружения
ENV DJANGO_SETTINGS_MODULE=todo.settings

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем requirements.txt в контейнер
COPY requirements.txt /app/

# Устанавливаем зависимости
RUN pip install -r requirements.txt

# Копируем все файлы проекта в контейнер
COPY . .

# Добавим текущую рабочую директорию в переменную PYTHONPATH
ENV PYTHONPATH /app

# Добавьте todoapp в sys.path
COPY todoapp /app/todoapp

# Создаем директорию для сбора статических файлов
RUN mkdir -p /static/

# Собираем статические файлы

# Команда для запуска сервера Django с автоперезагрузкой
CMD ["watchmedo", "auto-restart", "--", "python", "manage.py", "runserver", "0.0.0.0:8080"]
