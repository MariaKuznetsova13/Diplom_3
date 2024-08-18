import allure
from constants import Urls, Text
from locators.main_page_locators import MainPageLocators
from pages.account_page import AccountPage
from pages.main_page import MainPage
from pages.orders_list_page import OrdersList


class TestOrdersList:
    @allure.title('Проверка открытия всплывающего окна с деталями по клику на заказ')
    @allure.description('Проверяем, что по клику на заказ открывается попап с деталями заказа')
    def test_click_constructor_button(self, driver):
        page = OrdersList(driver)
        page.go_to_site(Urls.LIST_ORDERS)
        page.click_order()
        expected_result = page.get_compound_from_popup()
        assert expected_result == Text.TEXT_ORDER_COMPOUND

    @allure.title('Проверка, что заказы пользователя из раздела "История заказов" отображаются на странице "Лента '
                  'заказов"')
    @allure.description('Проверяем, что заказы пользователя из истории заказов в личном кабинете есть в ленте заказов')
    def test_number_orders_in_list(self, driver):
        create_order = MainPage(driver)
        create_order.go_to_site(Urls.MAIN_PAGE_URL)
        create_order.click_login_button()
        create_order.login_user()
        create_order.click_constructor_button()
        create_order.drag_and_drop()
        create_order.click_form_order_button()
        create_order.wait_for_element_invisible()
        create_order.click_close_order_button()
        create_order.click_login_button()
        account = AccountPage(driver)
        account.click_orders_history_button()
        account.wait_for_order_number()
        account_order_number = account.click_find_order_number()
        create_order.click_list_orders_button()
        orders_list = OrdersList(driver)
        list_order_number = orders_list.find_order_number_in_list(account_order_number)
        assert account_order_number == list_order_number

    @allure.title('Проверка счетчика Выполнено за всё время')
    @allure.description('Проверяем, что при создании нового заказа счётчик Выполнено за всё время увеличивается')
    def test_order_counter(self, driver):
        orders_list = OrdersList(driver)
        orders_list.go_to_site(Urls.LIST_ORDERS)
        orders_list.wait_for_all_orders()
        counter_before = orders_list.find_orders_for_all_time()
        account = AccountPage(driver)
        account.click_login_button()
        account.login_user()
        create_order = MainPage(driver)
        create_order.click_constructor_button()
        create_order.drag_and_drop()
        create_order.click_form_order_button()
        create_order.await_for_invisible_element(MainPageLocators.MODAL_ELEMENT)
        create_order.click_close_order_button()
        create_order.click_list_orders_button()
        orders_list.wait_for_all_orders()
        counter_after = orders_list.find_orders_for_all_time()
        assert counter_before < counter_after

    @allure.title('Проверка счетчика Выполнено за сегодня')
    @allure.description('Проверяем, что при создании нового заказа счётчик Выполнено за сегодня увеличивается')
    def test_order_counter_for_today(self, driver):
        orders_list = OrdersList(driver)
        orders_list.go_to_site(Urls.LIST_ORDERS)
        orders_list.wait_for_today_orders()
        counter_before = orders_list.find_orders_for_today()
        account = AccountPage(driver)
        account.click_login_button()
        account.login_user()
        create_order = MainPage(driver)
        create_order.click_constructor_button()
        create_order.drag_and_drop()
        create_order.click_form_order_button()
        create_order.wait_for_element_invisible()
        create_order.click_close_order_button()
        create_order.click_list_orders_button()
        orders_list.wait_for_today_orders()
        counter_after = orders_list.find_orders_for_today()
        assert counter_before < counter_after

    @allure.title('Проверка появления номера оформленного заказа в разделе В работе')
    @allure.description('Проверяем, что после оформления заказа его номер появляется в разделе В работе')
    def test_order_number_in_progress(self, driver):
        create_order = MainPage(driver)
        create_order.go_to_site(Urls.MAIN_PAGE_URL)
        create_order.click_login_button()
        create_order.login_user()
        create_order.click_constructor_button()
        create_order.drag_and_drop()
        create_order.click_form_order_button()
        create_order.wait_for_element_invisible()
        order_number = create_order.find_number_of_my_order()
        create_order.click_close_order_button()
        create_order.click_list_orders_button()
        orders_list = OrdersList(driver)
        order_number_in_progress = orders_list.find_order_number_in_work()
        assert order_number in order_number_in_progress
