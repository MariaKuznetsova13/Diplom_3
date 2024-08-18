# Diplom_3

## Тесты на сервис "Яндекс.Самокат"

### Структура проекта
- allure_results - папка с отчетом о тестировании
- locators - папка с локаторами
- pages - папка с методами для тестирования
- tests - папка с тестами
- constants.py - файл с константами
- conftest.py - фикстуры
- requirements.txt - файл с необходимыми библиотеками

### Запуск тестов
- Установка зависимостей - pip3 install -r requirements.txt
- Запуск тестов без отчета - pytest -v
- Запуск тестов с отчетом - pytest --alluredir=allure_results