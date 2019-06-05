import pytest
from selenium import webdriver


@pytest.fixture(scope="module")
def chrome_driver(request):
    driver = webdriver.Chrome()
    # Shutdown the webdriver instance after tests finish
    request.addfinalizer(lambda *args: driver.quit())

    return driver
