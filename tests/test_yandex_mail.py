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
    def test_yandex_mail(self, browser):
        link = 'https://mail.yandex.ru/'
        page = YaMailPage(browser, link)
        page.open()
        page.go_to_login_page()

        assert page.get_title() == 'Авторизация', 'Должна открыться страница авторизации'

        page.login_to_email(MAIL_LOGIN, MAIL_PASS)

        page.search_messages()

        assert len(page.messages) == MESSAGES_COUNT
        
        page.send_letter(SURNAME)

        time.sleep(5)
