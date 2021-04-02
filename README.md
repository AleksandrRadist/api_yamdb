# api_yamdb

REST API для сервиса YaMDb — базы отзывов о фильмах, книгах и музыке.

### Installing

Проект использует:
- django - https://www.djangoproject.com,
- django REST framework - https://www.django-rest-framework.org,
- Docker - https://www.docker.com/products/docker-desktop,
- docker-compose - https://docs.docker.com/compose/,
- PostgreSQL - https://www.postgresql.org,
- nginx - https://nginx.org/ru/.

### Чтобы запустить проект необходимо:

Создать и активировать виртуальное окружение:

    'python -m venv venv'
    'venv\Scripts\activate'

Установить зависимости: 

    'pip install -r requirements.txt'
    
Запустить миграции: 

    'python manage.py migrate

Cоздать суперпользователя:

    'python manage.py createsuperuser'

Запустит сервер:
    
    'python manage.py runserver'

### Authors

[Despair696](https://github.com/Despair696) - управление пользователями (Auth и Users): система регистрации и аутентификации, права доступа, работа с токеном, система подтверждения e-mail, поля.

[AleksandrRadist](https://github.com/AleksandrRadist) - категории (Categories), жанры (Genres) и произведения (Titles): модели, view и эндпойнты для них.

[gavr-v-t](https://github.com/gavr-v-t) - отзывы (Review) и комментарии (Comments): модели и view, эндпойнты, права доступа для запросов. Рейтинги произведений.




