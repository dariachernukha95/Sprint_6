import pytest
import allure
from pages.main_page import MainPage

class TestDropdownListOfAnswersToQuestions:

    @allure.title('Проверка выпадающего списка в разделе «Вопросы о важном».')
    @allure.description('Нажимаем на вопрос и проверяем, что открывается соответсвующий ему ответ.')
    @pytest.mark.parametrize(
        'number_in_question_or_answer_locator, result',
        [
            ['0', 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'],
            ['1', 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'],
            ['2', 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'],
            ['3', 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'],
            ['4', 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'],
            ['5', 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'],
            ['6', 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'],
            ['7', 'Да, обязательно. Всем самокатов! И Москве, и Московской области.']
        ]
    )
    def test_check_answers_to_questions(self,driver, number_in_question_or_answer_locator, result):
        main_page = MainPage(driver)
        main_page.get_answer(number_in_question_or_answer_locator)
        answer_text = main_page.get_answer(number_in_question_or_answer_locator)
        assert answer_text == result

class TestHeaderLogos:

    @allure.title('Проверка перехода на главную страницу сервиса Самокат при нажатии на лого Самокат.')
    @allure.description('Переходим на страницу оформления заказа и проверяем переход на главную страницу сайта при нажатии на лого.')
    def test_go_to_scooter_page_by_clicking_on_scooter_logo(self, driver):
        main_page = MainPage(driver)
        main_page.click_order_button_in_header()
        main_page.click_scooter_logo()
        scooter_url = 'https://qa-scooter.praktikum-services.ru/'
        assert driver.current_url == scooter_url

    @allure.title('Проверка редиректа на страницу Дзен при нажатии на лого Яндекс.')
    @allure.description('Нажимаем на лого Яндекс и проверяем редирект на главную страницу Дзен.')
    def test_click_yandex_logo(self, driver):
        main_page = MainPage(driver)
        main_page.click_yandex_logo()
        main_page.switch_to_new_page()
        main_page.find_dzen_logo()
        dzen_url = 'https://dzen.ru/?yredirect=true'
        assert driver.current_url == dzen_url