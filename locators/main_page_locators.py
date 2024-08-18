from selenium.webdriver.common.by import By


class MainPageLocators:
    CONSTRUCTOR_BUTTON = (By.LINK_TEXT, 'Конструктор')
    ORDERS_LIST_BUTTON = (By.LINK_TEXT, 'Лента Заказов')
    BURGER = (By.XPATH, '//a[@href="/ingredient/61c0c5a71d1f82001bdaaa6d"]')
    INGREDIENT_DETAILS_POPUP = (By.XPATH, ".//h2[text()='Детали ингредиента']")
    BUTTON_CLOSE_DETAILS_POPUP = (By.XPATH, ".//button[contains(@class, 'Modal_modal__close')]")
    CREATE_BURGER = (By.XPATH, ".//section[contains(@class, 'BurgerConstructor_basket')]")
    BURGER_COUNTER = (By.XPATH, ".//a[contains(@href, '/ingredient/61c0c5a71d1f82001bdaaa6d')]"
                                "//ancestor::p[contains(@class, 'counter_counter')]")
    FORM_ORDER_BUTTON = (By.XPATH, ".//button[text()='Оформить заказ']")
    TEXT_ORDER_SUCCESS = (By.XPATH, ".//p[text()='Ваш заказ начали готовить']")
    BUTTON_CLOSE_ORDER = (By.XPATH, ".//button[contains(@class, 'Modal_modal__close_modified')]")
    MODAL_ELEMENT = (By.XPATH, "//*[contains(@class, 'Modal_modal__loading')]"
                               "/following::div[@class='Modal_modal_overlay__x2ZCr']")
    ORDER_NUMBER = (By.CLASS_NAME, "Modal_modal__title_shadow__3ikwq")
