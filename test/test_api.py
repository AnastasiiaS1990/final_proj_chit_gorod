import allure
from selenium.webdriver.common.by import By
from selenium import webdriver
import final_proj_chit_gorod.coftest
#from pages.AuthApi import AuthApi
import requests

base_url = "https://web-gate.chitai-gorod.ru/api/v1/"
token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL3VzZXItcmlnaHQiLCJzdWIiOjgxMjE0MDEsImlhdCI6MTcyOTYyMTM0NSwiZXhwIjoxNzI5NjI0OTQ1LCJ0eXBlIjoyMH0.0EP8iidzthtNSozF3gVZVjogD_3n7d6QJ2ZNvmUxJm4"
#id_not_product = 1234456
# def test_auth()
#     AuthApi()

# получить токен 
def test_token():
    my_token = {
        'Authorization': ("Bearer " + token)
    }
    return my_token



##Позитивные проверки
#Поиск товара из рекомендованного 
def test_home():
    resp = requests.get(base_url + 'recommend/user?perPage=42&userRecommendVersion=1', headers=test_token())
    response_body = resp.json()["data"]["products"][0]
    ID_product = response_body["id"]
    assert resp.status_code == 200
    return ID_product


#Добавление товара в корзину
def test_new_basket():
    project = {
        "id": test_home(),
        "adData": {
             "item_list_name":"index",
             "product_shelf":""
        }
    }
    resp = requests.post(base_url + 'cart/product', json=project, headers=test_token())
    assert resp.status_code == 200

  
# Переход в корзину
def test_basket():
    resp = requests.get(base_url + 'cart', headers=test_token())
    response_body = resp.json()["products"][0]
    id_korzina = response_body["id"]
    assert resp.status_code == 200
    return id_korzina

   
#Увеличение товара в корзине
def test_plus_basket():
    project = [
        {
            "id": test_basket(),
            "quantity":4
            }
    ]
    resp = requests.put(base_url + 'cart', json=project, headers=test_token())
    assert resp.status_code == 200


#Удаление товара из корзины
def test_del_basket():
    id_korzina_str = str(test_basket())
    resp = requests.delete(base_url + 'cart/product/' + id_korzina_str, headers=test_token())
    assert resp.status_code == 204


##Негативные проверки
# Получаем не существующий ИД
id_not = test_home()
id_not_product = id_not + 10000000


#Добавление не существующего товара
def test_negativ_new_basket():
    project = {
        "id": id_not_product,
        "adData": {
             "item_list_name":"index",
             "product_shelf":""
        }
    }
    resp = requests.post(base_url + 'cart/product', json=project, headers=test_token())
    assert resp.status_code == 500


#Удаление товара из пустой корзины
def test_negativ_del_basket():
    id_korzina_str = str(id_not_product)
    resp = requests.delete(base_url + 'cart/product/' + id_korzina_str, headers=test_token())
    assert resp.status_code == 404