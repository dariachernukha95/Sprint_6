from selenium.webdriver.common.by import By

class OrderFormPageLocators:

    NAME_INPUT_FIELD = By.XPATH, '//input[@placeholder = "* Имя"]'
    SURNAME_INPUT_FIELD = By.XPATH, '//input[@placeholder = "* Фамилия"]'
    ADDRESS_INPUT_FIELD = By.XPATH, '//input[@placeholder = "* Адрес: куда привезти заказ"]'
    METRO_STATION_INPUT_FIELD = By.XPATH, '//input[@placeholder = "* Станция метро"]'
    METRO_STATION_SHCHELKOVSKAYA = By.XPATH, '//li/button[@value = "66"]'
    METRO_STATION_DINAMO = By.XPATH, '//li/button[@value = "28"]'
    TELEPHONE_INPUT_FIELD = By.XPATH, '//input[@placeholder = "* Телефон: на него позвонит курьер"]'
    NEXT_BUTTON = By.XPATH, '//div[contains(@class, "Order_NextButton")]/button[text() = "Далее"]'
    DATA_INPUT_FIELD = By.XPATH, '//input[@placeholder = "* Когда привезти самокат"]'
    RENTAL_PERIOD_FIELD = By.XPATH, '//div[@class = "Dropdown-placeholder" and text() = "* Срок аренды"]'
    RENTAL_PERIOD_IN_DROPDOWN_LIST = By.XPATH, '//div[@class = "Dropdown-option" and text() = "{}"]'
    SCOOTER_COLOR = By.XPATH, '//label[@for = "{}"]'
    COMMENT_INPUT_FIELD = By.XPATH, '//input[@placeholder = "Комментарий для курьера"]'
    ORDER_BUTTON = By.XPATH,'//div[contains(@class, "Order_Buttons")]/button[text() = "Заказать"]'
    YES_BUTTON = By.XPATH, '//button[text() = "Да"]'
    ORDER_INFORMATION_WINDOW = By.XPATH,'//div[contains(@class, "Order_ModalHeader")]'
