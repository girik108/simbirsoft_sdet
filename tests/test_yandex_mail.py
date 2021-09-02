import time
import os

from dotenv import load_dotenv
import allure

from pages.yandex_mail_page import YaMailPage


load_dotenv()

MAIL_LOGIN = os.getenv('YA_MAIL_LOGIN')
MAIL_PASS = os.getenv('YA_MAIL_PASS')
MESSAGES_COUNT = int(os.getenv('MESSAGES_COUNT'))
SURNAME = os.getenv('SURNAME')


class TestYandexMail():

    @allure.feature('Тест почты Yandex')
    @allure.story('Тестовое задание на вакансию - Разработчик в тестировании')
    def test_yandex_mail(self, browser):
        link = 'https://mail.yandex.ru/'
        page = YaMailPage(browser, link)

        with allure.step(f'Открываем страницу {link}. Переходим на страницу авторизации.'):
            page.open()
            page.go_to_login_page()
            assert page.get_title() == 'Авторизация', 'Должна открыться страница авторизации'

        with allure.step('Авторизуемся на сайте'):
            page.login_to_email(MAIL_LOGIN, MAIL_PASS)

        with allure.step('Получаем список тестовых сообщений. Проверяем их количество.'):
            page.search_messages()
            assert len(page.messages) == MESSAGES_COUNT, f'Количество сообщений должно быть {MESSAGES_COUNT}'

        with allure.step('Отправляем самому себе сообщение.'):
            page.send_letter(SURNAME)

        time.sleep(1)
