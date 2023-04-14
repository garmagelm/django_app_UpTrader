# Описание проекта

Это Django-приложение реализует древовидное меню с возможностью редактирования через стандартную админ-панель Django.
Меню хранятся в базе данных, и их можно легко добавлять на любую страницу с помощью пользовательского шаблонного тега {% draw_menu %}.
Активный пункт меню определяется на основе текущего URL, а для отрисовки каждого меню используется только один запрос к БД.

# Установка и настройка

Клонируйте репозиторий:

`$ git clone https://github.com/garmagelm/django_app_UpTrader`

# Создайте и активируйте виртуальное окружение:

`$ cd django_tree_menu`

`$ python3 -m venv venv`

`$ source venv/bin/activate`

# Установите зависимости:

`(venv) $ pip install -r requirements.txt`

# Примените миграции:

`(venv) $ python manage.py migrate`

# Создайте суперпользователя для доступа к админ-панели:

`(venv) $ python manage.py createsuperuser`

# Запустите сервер разработки:

`(venv) $ python manage.py runserver`


# Использование

1) Откройте админ-панель Django по адресу http://127.0.0.1:8000/admin/ и войдите с учетными данными суперпользователя.
2) В разделе "Menu App" добавьте новое меню и соответствующие пункты меню.
3) Для отображения меню на странице используйте шаблонный тег:
4) Сохраните изменения в шаблоне и проверьте результат на соответствующей странице.

# Особенности

1) Поддерживает несколько меню на одной странице.
2) Активный пункт меню определяется на основе текущего URL.
3) Меню можно создавать и редактировать через стандартную админ-панель Django.
4) Поддерживает явные URL-адреса и именованные URL-адреса.
5) Использует только один запрос к БД для отрисовки каждого меню.


Автор: Эльмира Зарипова https://github.com/garmagelm/
