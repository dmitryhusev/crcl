from urllib3.exceptions import MaxRetryError
import allure
from allure_commons.types import AttachmentType
from selenium.common.exceptions import WebDriverException
from selenium import webdriver
import pytest

opts = FirefoxOptions()
opts.add_argument("--headless")

@pytest.fixture
def browser():
    # url = 'http://34.67.99.81:4444/wd/hub'
    # capabilities = {
    #     'browserName': 'chrome',
    #     'enableVNC': True
    # }
    # driver = webdriver.Remote(url, capabilities)
    driver = webdriver.Firefox(options=opt)
    driver.set_window_size(1920, 1080)
    yield driver
    driver.quit()


def pytest_exception_interact(node):
    # TODO: when fails on fixtures

    try:
        driver = node.funcargs.get('browser')
        try:
            allure.attach(
                driver.get_screenshot_as_png(),
                'screenshot',
                AttachmentType.PNG
            )
            allure.attach(
                f'url: {driver.current_url}\ntitle: {driver.title}',
                'page url/title',
                AttachmentType.TEXT
            )
        except (MaxRetryError, WebDriverException):
            pass
    except AttributeError as e:
        print(str(e))
