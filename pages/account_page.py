import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators.account_page_locators import AccountPageLocators
from pages.base_page import BasePage
from constants import Urls


class AccountPage(BasePage):
    @allure.step('Кликаем на кнопку "Личный кабинет"')
    def click_account_button(self):
        self.click_login_button()

    @allure.step('Кликаем по кнопке "История заказов')
    def click_orders_history_button(self):
        self.click_element(AccountPageLocators.BUTTON_ORDERS_HISTORY)
        return self.find_element(AccountPageLocators.BUTTON_ORDERS_HISTORY).get_attribute('class')

    @allure.step('Кликаем по кнопке "Выход')
    def click_logout_button(self):
        self.click_element(AccountPageLocators.LOGOUT_BUTTON)

    @allure.step('Ожидаем урл страницы входа в аккаунт')
    def wait_login_url(self):
        WebDriverWait(self.driver, 15).until(EC.url_to_be(Urls.ACCOUNT_URL))

    @allure.step('Ищем номер заказ в истории заказов')
    def click_find_order_number(self):
        return self.get_text(AccountPageLocators.ORDER_NUMBER)

    @allure.step('Ожидаем отображения номера заказа')
    def wait_for_order_number(self):
        self.wait_element_located(AccountPageLocators.ORDER_NUMBER)
