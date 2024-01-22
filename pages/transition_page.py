import allure
import time

from pages.base_page import BasePage
from locators.locators import Locators


class TransitionPage(BasePage):
    @allure.step("Переход по логотипу Самокат")
    def transition_logo_scooter(self):
        self.find_element_located_click(Locators.LOGO_SCOOTER)
        return self.driver.current_url

    @allure.step("Переход по логотипу Яндекс")
    def transition_logo_yandex(self):
        self.find_element_located_click(Locators.LOGO_YANDEX)

    @allure.step("Переход на вторую вкладку")
    def switch_dzen(self):
        self.switch_window(Locators.LOGO_DZEN, 1)
