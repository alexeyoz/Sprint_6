import allure

from pages.transition_page import TransitionPage
from constants import Url


@allure.story('Проверка клика по логотипу')
class TestScooterYandex:
    @allure.title('Переход на Самокат')
    def test_logo_scooter(self, driver):
        transition_page = TransitionPage(driver)
        transition_page.go_to_site(Url.ORDER_PAGE)
        transition_page.transition_logo_scooter()
        current_url = transition_page.current_url()
        assert current_url == Url.BASE_URL

    @allure.title('Переход на DZEN')
    def test_logo_yandex(self, driver):
        transition_page = TransitionPage(driver)
        transition_page.go_to_site(Url.BASE_URL)
        transition_page.transition_logo_yandex()
        transition_page.switch_dzen()
        current_url = transition_page.current_url()
        assert 'https://dzen.ru/' in current_url

