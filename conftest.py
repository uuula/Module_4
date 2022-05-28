import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="Choose language: es or fr")


@pytest.fixture(scope="function")
def browser(request):
    select_language = request.config.getoption("language")
    if select_language == "en":
        print("\nstart chrome browser for test spanish version")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': select_language})
        browser = webdriver.Chrome(options=options)
    elif select_language == "fr":
        print("\nstart chrome browser for test french version")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': select_language})
        browser = webdriver.Chrome(options=options)
    else:
        raise pytest.UsageError("--language should be es or fr")
    yield browser
    print("\nquit browser..")
    browser.quit()