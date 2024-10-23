import allure
from pages.authPage import AuthPage


@allure.feature("Позитивные проверки")
@allure.title("Поиск товара на сайте Читай-город")
def test_search(driver):
    with allure.step("Инициализация страницы авторизации"):
        ui_page = AuthPage(driver)
    with allure.step("Поиск по запросу 'Гарри Поттер'"):
        ui_page.search()


@allure.feature("Позитивные проверки")
@allure.title("Добавление товара в корзину")
def test_basket(driver):
    with allure.step("Инициализация страницы авторизации"):
        ui_page = AuthPage(driver)
    with allure.step("Добавление книги в корзину"):
        ui_page.basket()


@allure.feature("Позитивные проверки")
@allure.title("Авторизация, отправка кода на номер")
def test_auth(driver):
    with allure.step("Инициализация страницы авторизации"):
        ui_page = AuthPage(driver)
    with allure.step("Открытие формы авторизации, ввлод номера телефона и отправка кода на телефон"):
        ui_page.auth()


@allure.feature("Негативные проверки")
@allure.title("Поиск не существующего товара")
def test_negativ_search(driver):
    with allure.step("Инициализация страницы авторизации"):
        ui_page = AuthPage(driver)
    with allure.step("Поиск не существующего товара"):
        ui_page.negativ_search()


@allure.feature("Негативные проверки")
@allure.title("Ввод в окно авторизации букв ")
def test_negativ_auth(driver):
    with allure.step("Инициализация страницы авторизации"):
        ui_page = AuthPage(driver)
    with allure.step("Клик по кнопке авторизации и ввод некорректного номера телефона"):
        ui_page.negativ_auth()
