# final_proj_chit_gorod

# Дипломная работа. Архитектура фреймворка
##  Сайт "Читай город"
### Столбкова Анастасия 
- [Ссылка на проект](https://stolbkova.yonote.ru/share/9d823f25-4393-4e86-9484-0583576bd988)

### Стек:
- selenium,
- requests,
- pytest,
- allure

### Шаги
1. Склонировать проект 'git clone git@github.com:AnastasiiaS1990/final_proj_chit_gorod.git'
2. Установить зависимости
3. Добавить в переменную "phone_number" в файле /authPage.py номер телефона РФ, в формате "без цифр 8 и 9"
4. Получить токен меняется каждый час (dev tools-application-cookie-"access-token"-"Bearer токен")
5. Добавить токен в переменную token в pages/conftest.py
6. Запустить тесты 'pytest' команда: pytest -s -v
7. Сгенерировать отчет 'allure generate allure-files -o allure-report'
8. Открыть отчет 'allure open allure-report'  -  allure serve allure-result

### Структура:
- ./test - тесты
- ./pages - описание страниц
- ./api - апи клиенты
- ./db - помощники для работы с БД

### Полезные ссылки 
- [Подсказка по markdown](https://www.markdownguide.org/basic-syntax/)
- [Генератор файла .gitignore](https://www.toptal.com/developers/gitignore)

### Библиотеки 
- pytest-8.3.3
- selenium 4.25.0
- webdriver-manager 4.0.2
- requests 2.32.3
- allure-pytest 2.13.5


