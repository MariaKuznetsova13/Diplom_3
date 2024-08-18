import allure
from pages.password_recovery_page import PasswordRecoveryPage
from constants import Urls, Text


class TestPasswordRecovery:
    @allure.title('Проверка клика на кнопку "Восстановить пароль"')
    @allure.description('Проверяем, что по клику на кнопку "Восстановить пароль" открывается страница восстановления '
                        'пароля')
    def test_password_recovery_button(self, driver):
        page = PasswordRecoveryPage(driver)
        page.go_to_site(Urls.MAIN_PAGE_URL)
        page.click_login_button()
        page.wait_button_password_recovery()
        page.go_to_recovery_button()
        page.click_button_password_recovery()
        current_url = page.get_current_url()
        assert current_url == Urls.PASSWORD_RECOVERY_URL

    @allure.title('Проверка ввода почты и клика на кнопку "Восстановить"')
    @allure.description(
        'Проверяем, что после ввода почты и клика на кнопку "Восстановить" открывается страница с вводом нового пароля')
    def test_email_and_recovery_button(self, driver):
        page = PasswordRecoveryPage(driver)
        page.go_to_site(Urls.MAIN_PAGE_URL)
        page.click_login_button()
        page.go_to_recovery_button()
        page.click_button_password_recovery()
        page.enter_email()
        page.click_button_recovery()
        expected_result = page.get_text_recovery_password()
        assert expected_result == Text.TEXT_RECOVERY

    @allure.title('Проверка активности поля "Пароль" после нажатия кнопки показать/скрыть')
    @allure.description(
        'Проверяем, что после нажатия на кнопку показать/скрыть пароль поле пароля становится активным')
    def test_show_hide_password_button(self, driver):
        page = PasswordRecoveryPage(driver)
        page.go_to_site(Urls.MAIN_PAGE_URL)
        page.click_login_button()
        page.go_to_recovery_button()
        page.click_button_password_recovery()
        page.enter_email()
        page.click_button_recovery()
        page.click_password_button_show_hide()
        assert page.wait_input_password_active()
