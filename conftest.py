import pytest
from selenium import webdriver


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    driver = None
    if request.param == "firefox":
        driver = webdriver.Firefox()
    elif request.param == "chrome":
        driver = webdriver.Chrome()

    yield driver
    driver.quit()
