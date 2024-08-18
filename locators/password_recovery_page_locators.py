from selenium.webdriver.common.by import By


class RecoveryPageLocators:
    NEW_PASSWORD_BUTTON = (By.XPATH, '//a[@href="/forgot-password"]')
    EMAIL_INPUT = (By.XPATH, ".//input[@type='text']")
    BUTTON_RECOVERY = (By.XPATH, ".//button[text()='Восстановить']")
    TEXT_RECOVERY = (By.XPATH, ".//h2[text()='Восстановление пароля']")
    INPUT_NEW_PASSWORD = (By.XPATH, ".//label[text()='Пароль']/../"
                                    "input[@type='password' and @name='Введите новый пароль']")
    VISIBLE_NEW_PASSWORD_BUTTON = (By.XPATH, ".//div[@class='input__icon input__icon-action']")
    INPUT_NEW_PASSWORD_ACTIVE = (By.XPATH, ".//div[contains(@class, 'input_status_active')]")
