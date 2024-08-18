import allure
from locators.orders_list_page_locators import OrdersListLocators
from pages.base_page import BasePage


class OrdersList(BasePage):
    @allure.step('Кликаем по заказу')
    def click_order(self):
        self.click_element(OrdersListLocators.ORDER)

    @allure.step('Извлекаем состав из попапа деталей заказа')
    def get_compound_from_popup(self):
        return self.get_text(OrdersListLocators.ORDER_COMPOUND)

    @allure.step('Ищем номер заказа в ленте')
    def find_order_number_in_list(self, order_id):
        elements = self.find_elements(OrdersListLocators.NUMBER_OF_ORDERS)
        for element in elements:
            if order_id == element.text:
                return element.text

    @allure.step('Ищем количество заказов за все время')
    def find_orders_for_all_time(self):
        return self.get_text(OrdersListLocators.COUNTER_FOR_ALL_TIME)

    @allure.step('Ищем количество заказов за сегодня')
    def find_orders_for_today(self):
        return self.get_text(OrdersListLocators.COUNTER_FOR_TODAY)

    @allure.step('Ищем номер заказа в работе')
    def find_order_number_in_work(self):
        self.wait_element_located(OrdersListLocators.ALL_READY_TEXT)
        self.await_for_invisible_element(OrdersListLocators.ALL_READY_TEXT)
        return self.get_text(OrdersListLocators.ORDERS_IN_WORK)

    @allure.step('Ожидаем отображения количества всех заказов')
    def wait_for_all_orders(self):
        self.wait_element_located(OrdersListLocators.COUNTER_FOR_ALL_TIME)

    @allure.step('Ожидаем отображения заказов за сегодня')
    def wait_for_today_orders(self):
        self.wait_element_located(OrdersListLocators.COUNTER_FOR_TODAY)
