import pytest
from selenium import webdriver


@pytest.fixture(scope='module')
def chrome_driver(request):
    driver = webdriver.Chrome()
    # Shutdown the webdriver instance upon completion of test run
    request.addfinalizer(lambda *args: driver.quit())

    return driver
