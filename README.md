# # Тестовое задание на вакансию Разработчик в тестировании.

## Как запустить тесты
1) Клонируйте репозитроий с проектом:
```
git clone git@github.com:girik108/simbirsoft_sdet.git

```
2) Установите зависимости. Сначала poetry.
```
pip3 install poetry
poetry shell
poetry install

```
4) В директории проекта, в папке test создайте файл .env, в котором пропишите следующие переменные окружения :
 - YA_MAIL_LOGIN=Логин 
 - YA_MAIL_PASS=Пароль
 - MESSAGES_COUNT=Количество тестовых сообщений
 - MESSAGE_SUBJECT=Simbirsoft Тестовое задание
 - SURNAME=Фамилия
 
3) С помощью docker-compose.yaml запустите Selenium Grid(Hub, Nodes):
```
docker-compose up
```
4)  В новом окне терминала запустите тест:
```
pytest -s -v --alluredir=allure_results  tests/test_yandex_mail.py
```

## Автор

**Гиматов Ирек**

* [github.com/girik108](https://github.com/girik108)
* [email](mailto:gimatovig@yandex.ru)

Проект запущен по адресу http://foodgram.gimatov.gq/
