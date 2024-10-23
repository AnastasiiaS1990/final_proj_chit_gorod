import allure
import requests
from conftest import authAPI


base_url = authAPI.base_url
token = authAPI.token
id_book = authAPI.id_book
id_not_product = authAPI.id_not_product


@allure.title("получить токен")
def test_token():
    with allure.step("Получение токена из переменной"):
        my_token = {
            'Authorization': ("Bearer " + token)
        }
        return my_token


@allure.feature("Позитивные проверки")
@allure.title("Добавление товара в корзину")
def test_new_basket():
    with allure.step("Отправка запроса на добавление в корзину ИД книги"):
        project = {
            "id": id_book,
            "adData": {
                "item_list_name": "index",
                "product_shelf": ""
            }
        }
    resp = requests.post(base_url + 'cart/product', json=project, headers=test_token())
    assert resp.status_code == 200


@allure.feature("Позитивные проверки")
@allure.title("Переход в корзину")
def test_basket():
    with allure.step("Переход в корзину"):
        resp = requests.get(base_url + 'cart', headers=test_token())
    with allure.step("Получение ИД товара в корзине"):
        response_body = resp.json()["products"][0]
        id_korzina = response_body["id"]
    assert resp.status_code == 200
    return id_korzina


@allure.feature("Позитивные проверки")
@allure.title("Увеличение товара в корзине")
def test_plus_basket():
    with allure.step("Отправка запроса с новым количеством товара"):
        project = [
            {
                "id": test_basket(),
                "quantity": 4
                }
        ]
    resp = requests.put(base_url + 'cart', json=project, headers=test_token())
    assert resp.status_code == 200


@allure.feature("Позитивные проверки")
@allure.title("Удаление товара из корзины")
def test_del_basket():
    with allure.step("Изменение ИД из числового формата в строковый"):
        id_korzina_str = str(test_basket())
    with allure.step("Отправка запроса на удаление товара"):
        resp = requests.delete(base_url + 'cart/product/' + id_korzina_str, headers=test_token())
    assert resp.status_code == 204


@allure.feature("Негативные проверки")
@allure.title("Добавление не существующего товара")
def test_negativ_new_basket():
    with allure.step("Отправка запроса на удаление товара с существующим ИД"):
        project = {
            "id": id_not_product,
            "adData": {
                "item_list_name": "index",
                "product_shelf": ""
            }
        }
    resp = requests.post(base_url + 'cart/product', json=project, headers=test_token())
    assert resp.status_code == 500


@allure.feature("Негативные проверки")
@allure.title("Удаление товара из пустой корзины")
def test_negativ_del_basket():
    with allure.step("Изменение ИД из числового формата в строковый"):
        id_korzina_str = str(id_not_product)
    with allure.step("Отправка запроса на удаление товара"):
        resp = requests.delete(base_url + 'cart/product/' + id_korzina_str, headers=test_token())
    assert resp.status_code == 404
