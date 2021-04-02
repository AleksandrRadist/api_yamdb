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

Запустить docker-compose:

    'docker-compose up'

При первом запуске для функционирования проекта обязательно выполнить миграции: 

    'docker-compose exec web python manage.py migrate'

Чтобы создать суперпользователя:

    'docker-compose exec web python manage.py createsuperuser'

Чтобы загрузить тестовые данные в базу данных:

    'docker-compose exec web python manage.py loaddata fixtures.json'

### Authors

[Despair696](https://github.com/Despair696) - управление пользователями (Auth и Users): система регистрации и аутентификации, права доступа, работа с токеном, система подтверждения e-mail, поля.

[AleksandrRadist](https://github.com/AleksandrRadist) - категории (Categories), жанры (Genres) и произведения (Titles): модели, view и эндпойнты для них.

[gavr-v-t](https://github.com/gavr-v-t) - отзывы (Review) и комментарии (Comments): модели и view, эндпойнты, права доступа для запросов. Рейтинги произведений.




