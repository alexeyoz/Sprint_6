from selenium.webdriver.common.by import By


class Locators:
    # поля страницы
    LOGO_YANDEX = (By.XPATH, ".//*[@alt='Yandex']")
    LOGO_SCOOTER = (By.XPATH, ".//*[@alt='Scooter']")
    LOGO_DZEN = (By.XPATH, ".//*[@tabindex='0']")

    COOKIES = (By.XPATH, ".//*[@id='rcc-confirm-button']")
