from selenium.webdriver.common.by import By

class MainPageLocators:
    ORDER_BUTTON_IN_HEADER = By.XPATH, '//div[contains(@class, "Header")]/button[text() = "Заказать"]'
    ORDER_BUTTON_ON_PAGE = By.XPATH, '//div[contains(@class, "Home_FinishButton")]/button[text() = "Заказать"]'
    SCOOTER_LOGO = By.XPATH, '//a[contains(@class, "Header_LogoScooter")]'
    YANDEX_LOGO = By.XPATH, '//a[contains(@class, "Header_LogoYandex")]'
    QUESTION = By.XPATH, '//div[@id = "accordion__heading-{}"]'
    ANSWER = By.XPATH, '//div[@id = "accordion__panel-{}"]'
    DZEN_LOGO = By.XPATH, '//div[@class = "dzen-layout--desktop-base-header__logoContainer-pu dzen-layout--desktop-base-header__isMorda-2n"]'