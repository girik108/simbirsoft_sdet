import pytest
from selenium import webdriver


# def pytest_addoption(parser):
#     parser.addoption('--browser_name', action='store', default='chrome',
#                      help='Choose browser: chrome or firefox')


@pytest.fixture(scope='class', params=('chrome', 'firefox'))
def browser(request):
    # browser_name = request.config.getoption('browser_name')
    # browser = None
    # if browser_name in ['chrome', 'firefox']:
    #     browser = webdriver.Remote(
    #         command_executor='http://127.0.0.1:4444/wd/hub',
    #         desired_capabilities={'browserName': browser_name,
    #                               'platform': 'LINUX',
    #                               'platformName': 'LINUX'})
    # else:
    #     raise pytest.UsageError('--browser_name should be chrome or firefox')
    browser = webdriver.Remote(
        command_executor='http://127.0.0.1:4444/wd/hub',
        desired_capabilities={
            'browserName': request.param,
            'platform': 'LINUX',
            'platformName': 'LINUX'
        }
    )

    yield browser
    print('\nquit browser..')
    browser.quit()
