from selenium.webdriver.common.by import By

from .base_page import BasePage


class YandexMailPage(BasePage):
    def go_to_login_page(self):
        login_button = self.browser.find_element(By.LINK_TEXT, 'Войти')
        login_button.click()