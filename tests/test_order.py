import pytest

from pages.order_page import *
from locators.order_locators import OrderLocators
from constants import *


@allure.story('Оформить заказ')
class TestOrder:
    @allure.title('Проверка оформления заказа')
    @pytest.mark.parametrize('button, test_data', [(OrderLocators.BUTTON_ORDER1, TestData1),
                                                   (OrderLocators.BUTTON_ORDER2, TestData2)])
    def test_order(self, driver, button, test_data):
        order_page = OrderPage(driver)
        order_page.go_to_site(Constants.BASE_URL)
        order_page.apply_cookies()
        order_page.click_order(button)
        order_page.data_entry_form_1(test_data)
        order_page.data_entry_form_2(test_data)
        result = order_page.order_confirmation()
        assert result == "Посмотреть статус"
