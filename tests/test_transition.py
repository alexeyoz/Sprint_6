import allure

from pages.transition_page import TransitionPage
from constants import Constants


@allure.story('Проверка клика по логотипу')
class TestScooterYandex:
    @allure.title('Переход на Самокат')
    def test_logo_scooter(self, driver):
        transition_page = TransitionPage(driver)
        transition_page.go_to_site(Constants.ORDER_PAGE)
        transition_page.transition_logo_scooter()
        result = transition_page.transition_logo_scooter()
        assert result == Constants.BASE_URL

    @allure.title('Переход на DZEN')
    def test_logo_yandex(self, driver):
        transition_page = TransitionPage(driver)
        transition_page.go_to_site(Constants.BASE_URL)
        transition_page.transition_logo_yandex()
        transition_page.switch_window(1)
        current_url = transition_page.current_url()
        assert 'https://dzen.ru/' in current_url
