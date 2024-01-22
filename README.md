# Sprint_6 
# _Тестирование Яндекс самокат_
* Основа для написания авто тестов — фреймворк pytest.
* Установить зависимости — pip install -r requirements.txt.
* Команда для запуска — pytest -v.
* Команда для формирования отчетов Allure — allure serve allure_results

_locators.py_

* Locators - общие локаторы

_order_locators.py_

* OrderLocators - локаторы для форм заказа

_questions_locators.py_

* QuestionsLocators - локаторы проверки вопросов о важном

_base_page.py_

* go_to_site - переход на сайт
* scrolldown - скроллирование по странице
* find_element_located_click - поиск и клик по элементу
* find_elements_located - поиск элемента
* current_url - получить адрес сайта
* find_element_located_input - поиск элемента и ввод данных
* apply_cookies - применить cookies

_order_page.py_

* TestData1 - данные для заказа 1
* TestData2 - данные для заказа 2
* click_order - клик по кнопке заказа
* data_entry_form_1 - ввод данных в первой форме и переход на вторую
* data_entry_form_2 - ввод оставшихся данных
* order_confirmation - проверка окна подтверждающего осуществление заказа

_questions_page.py_

* check_the_questions - проверка текста вопросов

_transition_page.py_

* transition_logo_scooter - переход по логотипу "Самокат"
* transition_logo_yandex - переход по логотипу "Яндекс"
* switch_window - переход на открывшуюся вкладку

_conftest.py_

* driver - Функция запуска драйвера

_constants.py_

* Constants - используемые ссылки




