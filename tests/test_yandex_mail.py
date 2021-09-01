import time
import os
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from dotenv import load_dotenv

from pages.yandex_mail_page import YandexMailPage


load_dotenv()

YA_MAIL_LOGIN = os.getenv('YA_MAIL_LOGIN')
YA_MAIL_PASS = os.getenv('YA_MAIL_PASS')


class TestYandexMail():
    def test_yandex_mail(self, browser):
        browser.get('https://mail.yandex.ru/')

        login_button = browser.find_element(By.LINK_TEXT, 'Войти')
        login_button.click()

        login_area = browser.find_element(By.ID, 'passp-field-login')
        login_area.send_keys(YA_MAIL_LOGIN)

        login_button = browser.find_element(By.ID, 'passp:sign-in')
        login_button.click()

        password_area = browser.find_element(By.ID, 'passp-field-passwd')
        password_area.send_keys(os.getenv('YA_MAIL_PASS'))

        login_button = browser.find_element(By.ID, 'passp:sign-in')
        login_button.click()
        # # Найдем кнопку, которая отправляет введенное решение
        # submit_button = driver.find_element_by_css_selector(".submit-submission")

        # # Скажем драйверу, что нужно нажать на кнопку. После этой команды мы должны увидеть сообщение о правильном ответе
        # submit_button.click()

        ali_messages = browser.find_elements(
            By.XPATH, '//span[@class="mail-MessageSnippet-Item mail-MessageSnippet-Item_subject"]/span[contains(text(), "Simbirsoft Тестовое задание")]')
        assert len(ali_messages) == 3, 'Wrong email count'

        message = ali_messages[0]
        message.click()
        # После выполнения всех действий мы должны не забыть закрыть окно браузера
        time.sleep(3)
