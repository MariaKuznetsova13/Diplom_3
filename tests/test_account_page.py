import allure
from constants import Urls
from pages.account_page import AccountPage


class TestAccount:
    @allure.title('Проверка клика на кнопку "Личный кабинет"')
    @allure.description('Проверяем, что по клику на кнопку "Личный кабинет" открывается страница входа в аккаунт')
    def test_click_account(self, driver):
        page = AccountPage(driver)
        page.go_to_site(Urls.MAIN_PAGE_URL)
        page.click_account_button()
        current_url = page.get_current_url()
        assert current_url == Urls.ACCOUNT_URL

    @allure.title('Проверка перехода в раздел "История заказов"')
    @allure.description('Проверяем, что по клику на кнопку "История заказов" открывается страница с историей заказов')
    def test_orders_history_section(self, driver):
        page = AccountPage(driver)
        page.go_to_site(Urls.MAIN_PAGE_URL)
        page.click_account_button()
        page.login_user()
        page.click_account_button()
        page.click_orders_history_button()
        current_url = page.get_current_url()
        assert current_url == Urls.ORDERS_HISTORY_URLS

    @allure.title('Проверка выхода из аккаунта')
    @allure.description('Проверяем, что по клику на кнопку "Выход" попадаем на страницу входа в аккаунт')
    def test_click_logout_button(self, driver):
        page = AccountPage(driver)
        page.go_to_site(Urls.MAIN_PAGE_URL)
        page.click_account_button()
        page.login_user()
        page.click_account_button()
        page.click_logout_button()
        page.wait_login_url()
        current_url = page.get_current_url()
        assert current_url == Urls.ACCOUNT_URL
