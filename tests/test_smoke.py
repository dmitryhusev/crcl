from screen import make_attachment
from time import sleep


def test_smoke_1(browser):
    browser.get('https://pytest-html.readthedocs.io/en/latest/user_guide.html')
    sleep(5)
    make_attachment(browser)


def test_smoke_2(browser):
    browser.get('https://booqua.de/basket.html')
    sleep(5)
    make_attachment(browser)
