import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(4)
    driver.maximize_window()
    yield driver
    driver.quit()


class authAPI:
    base_url = "https://web-gate.chitai-gorod.ru/api/v1/"
    token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3Mjk3OTY0NzIsImlhdCI6MTcyOTYyODQ3MiwiaXNzIjoiL2FwaS92MS9hdXRoL2Fub255bW91cyIsInN1YiI6IjcwNWM2NDNmODYxODY4OGJmNjY1ZWY2M2FhYTljZTk0OWM0ZGZmYTA3MTNiMmY1OGYzYjMwMTM5ZWQwNDJlMWYiLCJ0eXBlIjoxMH0.eIaeFvMQGNlIC55nOeDX70ri3_cnOziGbb9yf9nv5Tk"
    id_book = 3040433
    id_not = id_book  # Получаем не существующий ИД
    id_not_product = id_not + 10000000
