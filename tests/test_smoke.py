

def test_smoke_1(browser):
    browser.get('https://pytest-html.readthedocs.io/en/latest/user_guide.html')
    assert 1


def test_smoke_2(browser):
    browser.get('https://booqua.de/basket.html')
    assert 1
