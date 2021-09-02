from selenium.webdriver.common.by import By

from .base_page import BasePage
from .locators import YaMailPageLocators


class YaMailPage(BasePage):
    def go_to_login_page(self):
        login_button = self.browser.find_element(
            *YaMailPageLocators.LOGIN_LINK)
        login_button.click()

    def login_to_email(self, login, password):
        login_area = self.browser.find_element(*YaMailPageLocators.LOGIN_AREA)
        login_area.send_keys(login)

        login_button = self.browser.find_element(
            *YaMailPageLocators.LOGIN_BUTTON)
        login_button.click()

        password_area = self.browser.find_element(
            *YaMailPageLocators.PASSWORD_AREA)
        password_area.send_keys(password)

        login_button = self.browser.find_element(
            *YaMailPageLocators.LOGIN_BUTTON)
        login_button.click()

    def search_messages(self):
        self.messages = self.browser.find_elements(
            *YaMailPageLocators.TEST_MESSAGES)

    def send_letter(self, surname):
        account_menu = self.browser.find_element(*YaMailPageLocators.USER_NAME)
        account_menu.click()

        email = self.browser.find_element(*YaMailPageLocators.USER_EMAIL)
        email = email.text.strip()

        write_msg_button = self.browser.find_element(
            *YaMailPageLocators.WRITE_MSG_BUTTON)
        write_msg_button = write_msg_button.click()

        address_field = self.browser.find_element(
            *YaMailPageLocators.ADDRESS_FIELD)
        address_field.send_keys(email)

        subject_field = self.browser.find_element(
            *YaMailPageLocators.SUBJECT_FIELD)
        subject_field.click()
        subject_field.send_keys(f'Simbirsoft Тестовое задание.{surname}')

        email_text = self.browser.find_element(*YaMailPageLocators.EMAIL_AREA)
        email_text.click()
        email_text.send_keys(len(self.messages))

        email_send_button = self.browser.find_element(
            *YaMailPageLocators.EMAIL_SEND_BUTTON)
        email_send_button.click()