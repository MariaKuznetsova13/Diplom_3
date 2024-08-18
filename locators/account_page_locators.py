from selenium.webdriver.common.by import By


class AccountPageLocators:
    LOGIN_EMAIL = (By.NAME, 'name')
    LOGIN_PASSWORD = (By.NAME, 'Пароль')
    SIGNIN_BUTTON = (By.XPATH, '//button[text()="Войти"]')
    BUTTON_ORDERS_HISTORY = (By.XPATH, ".//a[text()='История заказов']")
    LOGOUT_BUTTON = (By.XPATH, '//button[text()="Выход"]')
    ORDER_NUMBER = (By.XPATH, '//*[contains(@class,"textBox")]//p[contains(@class,"digits-default")]')
