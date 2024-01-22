from selenium.webdriver.common.by import By


class OrderLocators:
    BUTTON_ORDER1 = (By.XPATH, ".//*[@class='Button_Button__ra12g']")
    BUTTON_ORDER2 = (By.XPATH, ".//*[@class='Home_FinishButton__1_cWm']")

    NAME = (By.XPATH, ".//*[@placeholder='* Имя']")
    SURNAME = (By.XPATH, ".//input[@placeholder = '* Фамилия']")
    ADDRESS = (By.XPATH, ".//input[@placeholder = '* Адрес: куда привезти заказ']")
    METRO_STATION = (By.XPATH, ".//input[@placeholder = '* Станция метро']")
    NAME_METRO = (By.XPATH, ".//li[@class='select-search__row']")
    NUMBER_FOR_COURIER = (By.XPATH, ".//input[@placeholder = '* Телефон: на него позвонит курьер']")
    BUTTON_NEXT = (By.XPATH, ".//*[text()='Далее']")
    DELIVERY_DATE = (By.XPATH, ".//input[@placeholder = '* Когда привезти самокат']")
    RENTAL_PERIOD = (By.XPATH, ".//div[text()='* Срок аренды']")
    RENTAL_PERIOD_DAY = (By.XPATH, ".//div[@class = 'Dropdown-menu']/div[text() = 'сутки']")
    COLOR_GREY = (By.XPATH, ".//input[@id='grey']")
    COMMENT_TO_COURIER = (By.XPATH, ".//*[@placeholder='Комментарий для курьера']")
    BUTTON_ORDER = (By.XPATH, ".//*[@class='Button_Button__ra12g Button_Middle__1CSJM']")
    PLACE_AN_ORDER = (By.XPATH, ".//*[text()='Да']")
    ORDER_STATUS = (By.XPATH, ".//*[text()='Посмотреть статус']")

