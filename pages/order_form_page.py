from pages.base_page import BasePage
from locators.order_form_page_locators import OrderFormPageLocators
import allure


class OrderFormPage(BasePage):

    @allure.step('Заполняем поле Имя в форме заказа')
    def fill_input_field_name(self, name):
        self.fill_input_field(OrderFormPageLocators.NAME_INPUT_FIELD, name)

    @allure.step('Заполняем поле Фамилия в форме заказа')
    def fill_input_field_surname(self, surname):
        self.fill_input_field(OrderFormPageLocators.SURNAME_INPUT_FIELD, surname)

    @allure.step('Заполняем поле Адрес: куда привезти заказ в форме заказа')
    def fill_input_field_address(self, address):
        self.fill_input_field(OrderFormPageLocators.ADDRESS_INPUT_FIELD, address)

    @allure.step('Заполняем поле Телефон: на него позвонит курьер в форме заказа')
    def fill_input_field_telephone(self, telephone):
        self.fill_input_field(OrderFormPageLocators.TELEPHONE_INPUT_FIELD, telephone)

    @allure.step('Выбираем станцию метро Щелковская')
    def choose_metro_station_shchelkovskaya(self, metro_station):
        self.fill_input_field(OrderFormPageLocators.METRO_STATION_INPUT_FIELD, metro_station)
        self.click_on_element(OrderFormPageLocators.METRO_STATION_SHCHELKOVSKAYA)

    @allure.step('Выбираем станцию метро Динамо')
    def choose_metro_station_dinamo(self, metro_station):
        self.fill_input_field(OrderFormPageLocators.METRO_STATION_INPUT_FIELD, metro_station)
        self.click_on_element(OrderFormPageLocators.METRO_STATION_DINAMO)

    @allure.step('Нажимаем кнопку Далее')
    def click_next_button(self):
        self.click_on_element(OrderFormPageLocators.NEXT_BUTTON)

    @allure.step('Выбираем дату доставки самоката')
    def choose_data(self, data):
        self.fill_input_field(OrderFormPageLocators.DATA_INPUT_FIELD, data)
        self.click_enter_button(OrderFormPageLocators.DATA_INPUT_FIELD)

    @allure.step('Выбираем срок аренды самоката')
    def choose_rental_period(self, data):
        self.click_on_element(OrderFormPageLocators.RENTAL_PERIOD_FIELD)
        formated_locator = self.format_locator(OrderFormPageLocators.RENTAL_PERIOD_IN_DROPDOWN_LIST, data)
        self.click_on_element(formated_locator)

    @allure.step('Выбираем цвет самоката')
    def choose_scooter_color(self, color):
        formated_locator = self.format_locator(OrderFormPageLocators.SCOOTER_COLOR, color)
        self.click_on_element(formated_locator)

    @allure.step('Заполняем поле Комментарий в форме заказа')
    def fill_input_field_comment(self, comment):
        self.fill_input_field(OrderFormPageLocators.COMMENT_INPUT_FIELD, comment)

    @allure.step('Нажимаем кнопку Заказать')
    def click_order_button(self):
        self.click_on_element(OrderFormPageLocators.ORDER_BUTTON)

    @allure.step('Подтверждаем оформление заказа')
    def confirm_order(self):
        self.click_on_element(OrderFormPageLocators.YES_BUTTON)

    @allure.step('Находим всплывающее окно с информацией о заказе')
    def find_order_information_window(self):
        return self.find_element_with_wait(OrderFormPageLocators.ORDER_INFORMATION_WINDOW)