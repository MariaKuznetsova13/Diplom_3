import allure
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from constants import TestCreds
from locators.account_page_locators import AccountPageLocators
from locators.base_page_locators import BasePageLocators


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Переход на сайт")
    def go_to_site(self, base_url):
        return self.driver.get(base_url)

    @allure.step("Ожидание появления элемента")
    def wait_element_located(self, locator):
        return WebDriverWait(self.driver, 60).until(EC.presence_of_element_located(locator))

    @allure.step("Ожидание отображения элемента")
    def wait_element_visible(self, locator):
        return WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator))

    @allure.step("Ожидание не отображения элемента")
    def await_for_invisible_element(self, locator):
        WebDriverWait(self.driver, 100).until(EC.invisibility_of_element(locator))

    @allure.step("Ожидание кликабельности элемента")
    def wait_element_clickable(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))

    @allure.step("Ожидание появления элемента")
    def find_element(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))

    @allure.step("Ожидание появления всех элементов")
    def find_elements(self, locator):
        return WebDriverWait(self.driver, 30).until(EC.presence_of_all_elements_located(locator))

    @allure.step('Кликаем по элементу')
    def click_element(self, locator):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    @allure.step('Кликаем по кнопке "Личный кабинет"')
    def click_login_button(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(BasePageLocators.BUTTON_ACCOUNT_HEADER))
        self.driver.find_element(*BasePageLocators.BUTTON_ACCOUNT_HEADER).click()

    @allure.step("Получаем текущий урл")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Скролл к нужному разделу")
    def go_to_section(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Заполнение поля")
    def enter_text(self, locator, text):
        self.driver.find_element(*locator).send_keys(text)

    @allure.step("Извлечение текста")
    def get_text(self, locator):
        return self.driver.find_element(*locator).text

    @allure.step("Получить элемент, если элемент существует")
    def check_is_elements_exist(self, locator):
        return True if self.driver.find_elements(*locator) is None else False

    @allure.step('Перемещаем элемент с одним локатором в другой локатор')
    def drag_and_drop_element(self, first_locator, second_locator):
        source = self.driver.find_element(*first_locator)
        destination = self.driver.find_element(*second_locator)
        ActionChains(self.driver).click_and_hold(source).move_to_element(destination).release().perform()

    @allure.step('Логинимся в личном кабинете')
    def login_user(self):
        self.enter_text(AccountPageLocators.LOGIN_EMAIL, TestCreds.TEST_EMAIL)
        self.enter_text(AccountPageLocators.LOGIN_PASSWORD, TestCreds.TEST_PASSWORD)
        self.click_element(AccountPageLocators.SIGNIN_BUTTON)
