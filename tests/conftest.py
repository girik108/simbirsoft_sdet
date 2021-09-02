import pytest
from selenium import webdriver


@pytest.fixture(scope='class', params=('chrome', 'firefox'))
def browser(request):
    browser = webdriver.Remote(
        command_executor='http://127.0.0.1:4444/wd/hub',
        desired_capabilities={
            'browserName': request.param,
            'platform': 'LINUX',
            'platformName': 'LINUX'
        }
    )

    yield browser
    browser.quit()
