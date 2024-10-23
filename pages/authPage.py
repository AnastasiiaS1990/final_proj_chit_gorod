from selenium.webdriver.remote.webdriver import WebDriver
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver = None
search_name = "Гарри Поттер"
search_name_negativ = "asdfghjkl"
phone_number = 679099922
phone_number_negativ = "qweertyuui"



class AuthPage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://www.chitai-gorod.ru")


class UIPage:
    def search(self, search):
        driver.find_element(By.CLASS_NAME, "header-search__input").send_keys(search_name)
        driver.find_element(By.CLASS_NAME, "header-search__input").send_keys(Keys.ENTER)
        driver.quit()