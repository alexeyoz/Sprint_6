import allure

from locators.order_locators import OrderLocators
from pages.base_page import BasePage
from constants import *


class OrderPage(BasePage):
    @allure.step('Клик по кнопке Оформить заказ')
    def click_order(self, button_order):
        self.find_element_located_click(button_order)

    @allure.step("Ввод данных в первой форме + переход на вторую")
    def data_entry_form_1(self, test_data):
        self.find_element_located_input(OrderLocators.NAME, TestData1.test_data[0])
        self.find_element_located_input(OrderLocators.SURNAME, TestData1.test_data[1])
        self.find_element_located_input(OrderLocators.ADDRESS, TestData1.test_data[2])
        self.find_element_located_input(OrderLocators.METRO_STATION, TestData1.test_data[3])
        self.find_element_located_click(OrderLocators.NAME_METRO)
        self.find_element_located_input(OrderLocators.NUMBER_FOR_COURIER, TestData1.test_data[4])
        self.find_element_located_click(OrderLocators.BUTTON_NEXT)

    @allure.step("Ввод данных во второй форме + окно подтверждения")
    def data_entry_form_2(self, test_data):
        self.find_element_located_input(OrderLocators.DELIVERY_DATE, TestData1.test_data[5])
        self.find_element_located_click(OrderLocators.COLOR_GREY)
        self.find_element_located_click(OrderLocators.RENTAL_PERIOD)
        self.find_element_located_click(OrderLocators.RENTAL_PERIOD_DAY)
        self.find_element_located_input(OrderLocators.COMMENT_TO_COURIER, TestData1.test_data[6])
        self.find_element_located_click(OrderLocators.BUTTON_ORDER)
        self.find_element_located_click(OrderLocators.PLACE_AN_ORDER)

    @allure.step("Проверка всплывающего окна с сообщением об успешном создании заказа")
    def order_confirmation(self):
        return self.find_element_located(OrderLocators.ORDER_STATUS).text

