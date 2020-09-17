# bricks
Проект по созданию api на Django ORM

## Структура проекта
Проект представляет из себя 2 приложения:

1. работа с сущностями здание и кирпичи. Ссылки для работы:

    http://127.0.0.1:8000/api/v1/app/building/ - создание записи о здании

    http://127.0.0.1:8000/api/v1/app/building/{id}/add-bricks/ - внесение записи о кирпичах для здания с идентификатором id

    http://127.0.0.1:8000/api/v1/app/stats/ - статистика по зданиям и кирпичам для них

2. работа с api hh.ru для отслеживания статистики станций метрополитена:

    http://127.0.0.1:8000/api/v1/metro/verificate/ - единственный метод, выдающий статистику по неизмененным, обновленным и удаленным станциям метро.

## Запуск
    1. Скачайте архив с проектом любым удобным вам способом
    2. Разархивируйте его
    3. перейдите в директорию проекта и выполните команду pip install -r requirements.txt (Для linux - pip3)
    4. выпоните команду python manage.py runserver
    5. авторизуйтесь по ссылке http://127.0.0.1:8000/admin/ (admin/admin)
    6. авторизуйтесь по ссылке http://127.0.0.1:8000/api-auth/ (admin/admin)
    7. После этого вам доступно API

