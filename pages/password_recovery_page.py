import allure
from locators.password_recovery_page_locators import RecoveryPageLocators
from pages.base_page import BasePage
from constants import TestCreds


class PasswordRecoveryPage(BasePage):
    @allure.step('Нажимаем на кнопку "Восстановить пароль"')
    def click_button_password_recovery(self):
        self.click_element(RecoveryPageLocators.NEW_PASSWORD_BUTTON)

    @allure.step('Ожидаем появления кнопки "Восстановить пароль"')
    def wait_button_password_recovery(self):
        self.wait_element_located(RecoveryPageLocators.NEW_PASSWORD_BUTTON)

    @allure.step('Ожидаем появления кнопки "Восстановить пароль"')
    def wait_button_password_recovery(self):
        self.wait_element_located(RecoveryPageLocators.NEW_PASSWORD_BUTTON)

    @allure.step("Скролл к кнопке 'Восстановить пароль")
    def go_to_recovery_button(self):
        self.go_to_section(RecoveryPageLocators.NEW_PASSWORD_BUTTON)

    @allure.step('Заполняем поле email')
    def enter_email(self):
        self.enter_text(RecoveryPageLocators.EMAIL_INPUT, TestCreds.TEST_EMAIL)

    @allure.step('Нажимаем на кнопку "Восстановить"')
    def click_button_recovery(self):
        self.click_element(RecoveryPageLocators.BUTTON_RECOVERY)

    @allure.step('Извлекаем текст на странице востановления пароля')
    def get_text_recovery_password(self):
        return self.get_text(RecoveryPageLocators.TEXT_RECOVERY)

    @allure.step('Нажимаем на кнопку скрыть/показать пароль')
    def click_password_button_show_hide(self):
        self.click_element(RecoveryPageLocators.VISIBLE_NEW_PASSWORD_BUTTON)

    @allure.step('Ожидаем, когда поле пароля станет активным')
    def wait_input_password_active(self):
        return self.wait_element_visible(RecoveryPageLocators.INPUT_NEW_PASSWORD_ACTIVE)
