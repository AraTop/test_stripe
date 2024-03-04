FROM python:3

# Установка переменной среды PYTHONUNBUFFERED, чтобы выводить логи stdout/stderr в реальном времени без буферизации
ENV PYTHONUNBUFFERED=1

# Создание и установка рабочей директории в Docker контейнере
WORKDIR /code

# Копирование зависимостей проекта в Docker контейнер
COPY requirements.txt /code/
RUN pip install -r requirements.txt

# Копирование всех файлов проекта в Docker контейнер
COPY . .

# Команда для создания и применения миграций Django
RUN python manage.py makemigrations
RUN python manage.py migrate

# Команда для запуска Django приложения в контейнере
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]