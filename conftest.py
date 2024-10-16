import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    url = 'https://qa-scooter.praktikum-services.ru/'
    driver.get(url)
    yield driver
    driver.quit()