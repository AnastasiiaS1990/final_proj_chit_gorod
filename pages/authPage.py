from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


# Данные для теста
search_name = "Незнайка"
search_id = 3062121
search_name_negativ = "asdfghjkl"
phone_number = 1 # Добавить в переменную "phone_number" в файле /authPage.py номер телефона РФ, в формате "без цифр 8 и 9"
phone_number_negativ = "qweertyuui"


class AuthPage:
    @allure.title("метод для иницилизации")
    def __init__(self, driver):
        self.driver = driver
        with allure.step("Переход на сайт"):
            self.driver.get("https://www.chitai-gorod.ru")
    
    @allure.feature("Позитивные проверки")
    @allure.title("метод для поиска товара")
    def search(self):
        with allure.step("Найти поле поиска и ввести запрос"):
            search_field = self.driver.find_element(By.CLASS_NAME, "header-search__input")
            search_field.send_keys(search_name)
            search_field.send_keys(Keys.ENTER)
        with allure.step("Закрыть браузер после выполнения поиска"):
            self.driver.quit()


    @allure.title("Метод для добавления товара в корзину")
    def basket(self):
        with allure.step("Найти поле поиска и ввести запрос"):
            search_field = self.driver.find_element(By.CLASS_NAME, "header-search__input")
            search_field.send_keys(search_id)
            search_field.send_keys(Keys.ENTER)
        sleep(5)  # используется слиип, т.к. WebDriverWait не отрабатывает, пробовала много раз и заные варианты
        with allure.step("Добавить книгу в корзину"):
            basket_field = self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/section[1]/section[1]/div[1]/article[1]/div[3]/div[1]")
        # basket_field = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "article[class='product-card product-card product'] div[class='button action-button blue']")))
            basket_field.click()
        with allure.step("Закрыть браузер после добавления товара в корзину"):
            self.driver.quit()


    @allure.title("метод для авторизации")
    def auth(self):
        with allure.step("Открыть форму авторизации"):
            auth_field = self.driver.find_element(By.CSS_SELECTOR, ".header-profile__button")
            auth_field.click()
        with allure.step("Ввести номер телефона"):
            input_field = self.driver.find_element(By.CLASS_NAME, "phone-input__input")
            input_field.send_keys(phone_number)
        with allure.step("Нажать кнопку 'Получить код'"):
            buy_button = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "app-button-text")))
            buy_button.click()
        with allure.step("Закрыть браузер после отправки кода"):
            self.driver.quit()


    @allure.feature("Негативные проверки")
    @allure.title("метод для поиска не существующего товара")
    def negativ_search(self):
        with allure.step("Найти поле поиска и ввести запрос"):
            negativ_search_field = self.driver.find_element(By.CLASS_NAME, "header-search__input")
            negativ_search_field.send_keys(search_name_negativ)
            negativ_search_field.send_keys(Keys.ENTER)
        with allure.step("Ожидание появления элемента на странице до 10 секунд"):
            try:
                WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[3]/div[1]/section[1]/div[1]/div[1]/h4[1]")))
                print("Элемент найден на странице!")
            except:
                print("Элемент не найден на странице.")
            finally:
                with allure.step("Закрыть браузер после выполнения поиска"):
                    self.driver.quit()


    @allure.title("метод для авторизации с неверным форматом телефона")
    def negativ_auth(self):
        with allure.step("Клик по кнопке авторизации"):
            negativ_auth_field = self.driver.find_element(By.CSS_SELECTOR, ".header-profile__button")
            negativ_auth_field.click()
        with allure.step("Ввод некорректного номера телефона"):
            negativ_input_field = self.driver.find_element(By.CLASS_NAME, "phone-input__input")
            negativ_input_field.send_keys("fsgfdgdfh")
        with allure.step("Проверка кликабельности кнопки"):
            try:
                button = self.driver.find_element(By.CLASS_NAME, "app-button-text")
                if button.is_enabled():
                    print("Кнопка кликабельна")
                else:
                    print("Кнопка не кликабельна")
            finally:
                with allure.step("Закрыть браузер после выполнения проверки"):
                    self.driver.quit()
