from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def click_on_element(self,locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator))
        self.driver.find_element(*locator).click()

    def fill_input_field(self, locator, text):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator))
        self.driver.find_element(*locator).send_keys(text)

    def format_locator(self, full_locator, value):
        method, locator = full_locator
        locator = locator.format(value)
        return method, locator

    def click_enter_button(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator))
        self.driver.find_element(*locator).send_keys(Keys.ENTER)

    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text
#
    def scroll_to_element(self, locator):
        element = self.find_element_with_wait(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def switch_to_new_page(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])