import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en')


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    browser = webdriver.Chrome()
    print("\nopen browser..")
    yield browser
    print("\nquit browser..")
    browser.quit()