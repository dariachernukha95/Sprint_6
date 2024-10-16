from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
import allure

class MainPage(BasePage):

    @allure.step('Нажимаем на кнопку Заказать в хедере')
    def click_order_button_in_header(self):
        self.click_on_element(MainPageLocators.ORDER_BUTTON_IN_HEADER)

    @allure.step('Нажимаем на кнопку Заказать внизу главной страницы')
    def click_order_button_on_page(self):
        self.scroll_to_element(MainPageLocators.ORDER_BUTTON_ON_PAGE)
        self.click_on_element(MainPageLocators.ORDER_BUTTON_ON_PAGE)

    @allure.step('Нажимаем на логотип Самокат в хедере')
    def click_scooter_logo(self):
        self.click_on_element(MainPageLocators.SCOOTER_LOGO)

    @allure.step('Нажимаем на логотип Яндекс в хедере')
    def click_yandex_logo(self):
        self.click_on_element(MainPageLocators.YANDEX_LOGO)

    @allure.step('Переключаемся на последнюю открытую вкладку')
    def switch_to_last_tab(self):
        self.switch_to_new_page()

    @allure.step('Переключаемся на последнюю открытую вкладку')
    def find_dzen_logo(self):
        self.find_element_with_wait(MainPageLocators.DZEN_LOGO)

    @allure.step('Получаем ответ на выбранный вопрос')
    def get_answer(self, number_in_question_or_answer_locator):
        formated_question_locator = self.format_locator(MainPageLocators.QUESTION, number_in_question_or_answer_locator)
        self.scroll_to_element(formated_question_locator)
        self.click_on_element(formated_question_locator)
        formated_answer_locator = self.format_locator(MainPageLocators.ANSWER, number_in_question_or_answer_locator)
        answer_text = self.get_text_from_element(formated_answer_locator)
        return answer_text