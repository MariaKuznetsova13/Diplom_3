import allure
from constants import Urls, Text
from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators


class TestMainPage:
    @allure.title('Проверка клика на кнопку "Конструктор"')
    @allure.description('Проверяем, что по клику на кнопку "Конструктор" открывается главная страница с конструктором')
    def test_click_constructor_button(self, driver):
        page = MainPage(driver)
        page.go_to_site(Urls.MAIN_PAGE_URL)
        page.click_login_button()
        page.click_constructor_button()
        current_url = page.get_current_url()
        assert current_url == Urls.MAIN_PAGE_URL

    @allure.title('Проверка клика на кнопку "Лента заказов"')
    @allure.description('Проверяем, что по клику на кнопку "Лента заказов" открывается страница с заказами')
    def test_click_list_orders_button(self, driver):
        page = MainPage(driver)
        page.go_to_site(Urls.MAIN_PAGE_URL)
        page.click_list_orders_button()
        current_url = page.get_current_url()
        assert current_url == Urls.LIST_ORDERS

    @allure.title('Проверка клика на ингредиент')
    @allure.description('Проверяем, что по клику на ингредиент открывается попап с деталями ингредиента')
    def test_click_ingredient(self, driver):
        page = MainPage(driver)
        page.go_to_site(Urls.MAIN_PAGE_URL)
        page.click_ingredient_button()
        expected_result = page.get_text_from_ingredient_popup()
        assert expected_result == Text.TEXT_INGREDIENTS

    @allure.title('Проверка клика на кнопку закрытия попапа с деталями ингредиента')
    @allure.description('Проверяем, что по клику на крестик, попап с деталями ингредиента закрывается')
    def test_close_ingredient(self, driver):
        page = MainPage(driver)
        page.go_to_site(Urls.MAIN_PAGE_URL)
        page.click_ingredient_button()
        page.close_ingredient_button()
        assert not page.check_is_elements_exist(MainPageLocators.INGREDIENT_DETAILS_POPUP)

    @allure.title('Проверка увеличения каунтера при добавлении ингредиента')
    @allure.description('Проверяем, что при добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента')
    def test_close_ingredient(self, driver):
        page = MainPage(driver)
        page.go_to_site(Urls.MAIN_PAGE_URL)
        page.drag_and_drop()
        expected_result = page.check_counter_ingredient()
        assert expected_result == '2'

    @allure.title('Проверка клика на кнопку "Оформить заказ" залогиненным пользователем')
    @allure.description('Проверяем, что по клику на кнопку "Оформить заказ" залогиненным пользователем открывается '
                        'попап с текстом о принятом заказе')
    def test_click_order_form_button(self, driver):
        page = MainPage(driver)
        page.go_to_site(Urls.MAIN_PAGE_URL)
        page.click_login_button()
        page.login_user()
        page.click_constructor_button()
        page.drag_and_drop()
        page.click_form_order_button()
        expected_result = page.get_text_formed_order_popup()
        assert expected_result == Text.TEXT_ORDER_SUCCESS
