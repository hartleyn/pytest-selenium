import pytest
from selenium import webdriver


@pytest.fixture(scope="module")
def chrome_driver(request):
    driver = webdriver.Chrome()

    request.addfinalizer(lambda *args: driver.quit())

    return driver
