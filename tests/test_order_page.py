import allure
from pages.main_page import MainPage
from pages.order_form_page import OrderFormPage

class TestLogIn:

    @allure.title('Проверка оформления заказа через кнопку Заказать внизу страницы.')
    @allure.description('Заполняем все поля формы заказа, подтверждаем оформление заказа и проверяем появление всплывающего окна с информацией о заказе.')
    def test_login_by_login_button_on_main_page(self,driver):
        main_page = MainPage(driver)
        order_form_page = OrderFormPage(driver)
        main_page.click_order_button_on_page()
        order_form_page.fill_input_field_name('Дарья')
        order_form_page.fill_input_field_surname('Чернуха')
        order_form_page.fill_input_field_address('Щёлковское ш., 75, Москва')
        order_form_page.fill_input_field_telephone('+79106578930')
        order_form_page.choose_metro_station_shchelkovskaya('Щёлковская')
        order_form_page.click_next_button()
        order_form_page.choose_data('19.10.2024')
        order_form_page.choose_rental_period('пятеро суток')
        order_form_page.choose_scooter_color('black')
        order_form_page.fill_input_field_comment('Прошу привезти к 12:00')
        order_form_page.click_order_button()
        order_form_page.confirm_order()
        order_information_window_text = order_form_page.find_order_information_window().text
        assert 'Заказ оформлен' in order_information_window_text


    @allure.title('Проверка оформления заказа через кнопку Заказать в хедере страницы.')
    @allure.description('Заполняем все поля формы заказа, подтверждаем оформление заказа и проверяем появление всплывающего окна с информацией о заказе.')
    def test_login_by_login_button_in_header(self, driver):
        main_page = MainPage(driver)
        order_form_page = OrderFormPage(driver)
        main_page.click_order_button_in_header()
        order_form_page.fill_input_field_name('Иван')
        order_form_page.fill_input_field_surname('Иванов')
        order_form_page.fill_input_field_address('Ленинградский просп., 36, Москва')
        order_form_page.fill_input_field_telephone('89106673034')
        order_form_page.choose_metro_station_dinamo('Динамо')
        order_form_page.click_next_button()
        order_form_page.choose_data('10.11.2024')
        order_form_page.choose_rental_period('трое суток')
        order_form_page.choose_scooter_color('grey')
        order_form_page.fill_input_field_comment('')
        order_form_page.click_order_button()
        order_form_page.confirm_order()
        order_information_window_text = order_form_page.find_order_information_window().text
        assert 'Заказ оформлен' in order_information_window_text
