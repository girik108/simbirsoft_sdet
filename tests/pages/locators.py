from selenium.webdriver.common.by import By


class YaMailPageLocators():
    LOGIN_LINK = (By.LINK_TEXT, 'Войти')
    LOGIN_AREA = (By.ID, 'passp-field-login')
    LOGIN_BUTTON = (By.ID, 'passp:sign-in')
    PASSWORD_AREA = (By.ID, 'passp-field-passwd')
    TEST_MESSAGES = (By.XPATH, '//span[@class="mail-MessageSnippet-Item mail-MessageSnippet-Item_subject"]/span[contains(text(), "Simbirsoft Тестовое задание")]')
    FORWARD_BUTTON = (By.XPATH, '//span[@class="mail-Toolbar-Item-Text js-toolbar-item-title js-toolbar-item-title-reply"]')
    USER_NAME = (By.CSS_SELECTOR, 'span.user-account__name:nth-child(1)')
    USER_EMAIL = (By.CSS_SELECTOR, 'span.user-account__subname:nth-child(1)')
    WRITE_MSG_BUTTON = (By.CSS_SELECTOR, 'span.mail-ComposeButton-Text')

    ADDRESS_FIELD = (By.CSS_SELECTOR, '.ComposeRecipients-ToField > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1)')
    SUBJECT_FIELD = (By.CLASS_NAME, 'composeTextField')
    EMAIL_AREA = (By.CSS_SELECTOR, '.cke_wysiwyg_div')
    EMAIL_SEND_BUTTON = (By.CLASS_NAME, 'ComposeControlPanelButton-Button_action')