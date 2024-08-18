from selenium.webdriver.common.by import By


class OrdersListLocators:
    ORDER = (By.XPATH, ".//ul[contains(@class, 'OrderFeed_list')]/li[1]/a")
    ORDER_COMPOUND = (By.XPATH, ".//p[text()='Cостав']")
    NUMBER_OF_ORDERS = (By.XPATH, '//div[@class="OrderHistory_textBox__3lgbs mb-6"]//p[@class="text '
                                  'text_type_digits-default"]')
    COUNTER_FOR_ALL_TIME = (By.XPATH, '//p[text()="Выполнено за все время:"]/following-sibling::p')
    COUNTER_FOR_TODAY = (By.XPATH, '//p[text()="Выполнено за сегодня:"]/following-sibling::p')
    ORDERS_IN_WORK = (By.XPATH, '//*[contains(@class,"orderListReady")]//li[contains(@class,"digits-default")]')
    ALL_READY_TEXT = (By.XPATH, '//li[text()="Все текущие заказы готовы!"]')
