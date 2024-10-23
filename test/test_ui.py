from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from pages.authPage import AuthPage
from pages.authPage import UIPage
from time import sleep
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

search_name = "Гарри Поттер"
search_name_negativ = "asdfghjkl"
phone_number = 679099922
phone_number_negativ = "qweertyuui"

## Позитивные проверки
# Поиск товара через строку поиска на русском языке
def test_search():
    AuthPage() 
    UIPage.search()

    # driver = webdriver.Chrome()
    # driver.get("https://www.chitai-gorod.ru")
    #driver.find_element(By.CLASS_NAME, "header-search__input").clear()
    # driver.find_element(By.CLASS_NAME, "header-search__input").send_keys(search_name)
    # driver.find_element(By.CLASS_NAME, "header-search__input").send_keys(Keys.ENTER)
    #form = AuthPage(driver)
    #form.search("Гарри Поттер")
    #sleep(10)
    # driver.quit()


# Добавление товара в корзину
def test_basket():
    driver = webdriver.Chrome()
    driver.get("https://www.chitai-gorod.ru")
    #buy_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".action-button__text")))
    #buy_button.click()
    #driver.find_element(By.CSS_SELECTOR, ".action-button__text").click()
    driver.find_element(By.CLASS_NAME, "header-search__input").send_keys(search_name)
    driver.find_element(By.CLASS_NAME, "header-search__input").send_keys(Keys.ENTER)
    sleep(5)
    # ОЖИДАНИЕ
    driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/section[1]/section[1]/div[1]/article[1]/div[3]/div[1]").click()
    #driver.get("https://www.chitai-gorod.ru/cart")
    sleep(5)
    driver.quit()

# Авторизация, отправка кода на номер
def test_auth():
    driver = webdriver.Chrome()
    driver.get("https://www.chitai-gorod.ru")
    driver.find_element(By.CSS_SELECTOR, ".header-profile__button").click()
    driver.find_element(By.CLASS_NAME, "phone-input__input").send_keys(phone_number)
    buy_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "app-button-text")))
    buy_button.click()
    sleep(5)
    driver.quit()


## Негативные проверки
# Поиск не существующего товара
def test_negativ_search():
    driver = webdriver.Chrome()
    driver.get("https://www.chitai-gorod.ru")
    #driver.find_element(By.CLASS_NAME, "header-search__input").clear()
    driver.find_element(By.CLASS_NAME, "header-search__input").send_keys(search_name_negativ)
    driver.find_element(By.CLASS_NAME, "header-search__input").send_keys(Keys.ENTER)
    sleep(5)
    try: # Ожидание появления элемента на странице до 10 секунд 
        element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[3]/div[1]/section[1]/div[1]/div[1]/h4[1]")) ) 
        print("Элемент найден на странице!") 
    except: 
        print("Элемент не найден на странице.") 
    finally: # Закрытие браузера 
        driver.quit()

# Ввод в окно авторизации букв 
def test_negativ_auth():
    driver = webdriver.Chrome()
    driver.get("https://www.chitai-gorod.ru")
    driver.find_element(By.CSS_SELECTOR, ".header-profile__button").click()
    driver.find_element(By.CLASS_NAME, "phone-input__input").send_keys(phone_number_negativ)
    try:
        button = driver.find_element(By.CLASS_NAME, "app-button-text")
        if button.is_enabled():
            print("Кнопка кликабельна")
        else: 
            print("Кнопка не кликабельна")
    finally:
        driver.quit()  



