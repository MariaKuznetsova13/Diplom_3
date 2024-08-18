import allure
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    @allure.step('Кликаем по кнопке "Конструктор"')
    def click_constructor_button(self):
        self.click_element(MainPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step('Кликаем по кнопке "Лента заказов"')
    def click_list_orders_button(self):
        self.click_element(MainPageLocators.ORDERS_LIST_BUTTON)

    @allure.step('Кликаем по ингредиенту')
    def click_ingredient_button(self):
        self.click_element(MainPageLocators.BURGER)

    @allure.step('Извлекаем текст из попапа ингредиента')
    def get_text_from_ingredient_popup(self):
        return self.get_text(MainPageLocators.INGREDIENT_DETAILS_POPUP)

    @allure.step('Кликаем по кнопку закрытия попапа с деталями ингредиента')
    def close_ingredient_button(self):
        self.click_element(MainPageLocators.BUTTON_CLOSE_DETAILS_POPUP)

    @allure.step('Перетаскиваем ингредиент для создания бургера')
    def drag_and_drop(self):
        self.wait_element_visible(MainPageLocators.BURGER)
        self.drag_and_drop_element(MainPageLocators.BURGER, MainPageLocators.CREATE_BURGER)

    @allure.step('Ожидаем не отображения модального элемента')
    def wait_for_element_invisible(self):
        self.await_for_invisible_element(MainPageLocators.MODAL_ELEMENT)

    @allure.step('Извлекаем текст из попапа оформленного заказа')
    def get_text_formed_order_popup(self):
        return self.get_text(MainPageLocators.TEXT_ORDER_SUCCESS)

    @allure.step('Проверяем число каунтера')
    def check_counter_ingredient(self):
        self.wait_element_visible(MainPageLocators.BURGER)
        return self.get_text(MainPageLocators.BURGER_COUNTER)

    @allure.step('Кликаем по кнопке "Оформить заказ"')
    def click_form_order_button(self):
        self.click_element(MainPageLocators.FORM_ORDER_BUTTON)

    @allure.step('Закрываем детали оформленного заказа')
    def click_close_order_button(self):
        self.click_element(MainPageLocators.BUTTON_CLOSE_ORDER)

    @allure.step('Ищем номер своего заказа')
    def find_number_of_my_order(self):
        return self.get_text(MainPageLocators.ORDER_NUMBER)
