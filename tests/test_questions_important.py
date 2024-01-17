# import allure
import pytest

from pages.questions_page import QuestionsPage
from locators.questions_locators import QuestionsLocators
from constants import Constants

list_questions = [[QuestionsLocators.QUESTION_1, QuestionsLocators.QUESTION_1_TEXT,
                   'Сутки — 400 рублей. Оплата курьеру — наличными или картой.']]
                  # [QuestionsLocators.QUESTION_2, QuestionsLocators.QUESTION_2_TEXT,
                  #  'Пока что у нас так: один заказ — один самокат. '
                  #  'Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'],
                  # [QuestionsLocators.QUESTION_3, QuestionsLocators.QUESTION_3_TEXT,
                  #  'Допустим, вы оформляете заказ на 8 мая. '
                  #  'Мы привозим самокат 8 мая в течение дня. '
                  #  'Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. '
                  #  'Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'],
                  # [QuestionsLocators.QUESTION_4, QuestionsLocators.QUESTION_4_TEXT,
                  #  'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'],
                  # [QuestionsLocators.QUESTION_5, QuestionsLocators.QUESTION_5_TEXT,
                  #  'Пока что нет! ''Но если что-то срочное — всегда можно позвонить '
                  #  'в поддержку по красивому номеру 1010.'],
                  # [QuestionsLocators.QUESTION_6, QuestionsLocators.QUESTION_6_TEXT,
                  #  'Самокат приезжает к вам с полной зарядкой. '
                  #  'Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. '
                  #  'Зарядка не понадобится.'],
                  # [QuestionsLocators.QUESTION_7, QuestionsLocators.QUESTION_7_TEXT,
                  #  'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. '
                  #  'Все же свои.'],
                  # [QuestionsLocators.QUESTION_8, QuestionsLocators.QUESTION_8_TEXT,
                  #  'Да, обязательно. Всем самокатов! И Москве, и Московской области.']]


class TestQuestions:
    def __init__(self):
        pass

    #@pytest.mark.parametrize('question_locator,question_text_locator, text', list_questions)
    def test__questions(self, driver, question_locator, question_text_locator, text):
        questions_page = QuestionsPage(driver)
        questions_page.go_to_site(Constants.BASE_URL)







        # questions_page = QuestionsPage(driver)  # объект класса
        # questions_page.go_to_site(Constants.BASE_URL)  # стартовая страница
        # questions_page.scrolldown_question(question_locator)  # прокрутка до вопросов
        # questions_page.click_questions(question_locator)  # клик по вопросу
        # correct_text = questions_page.get_text_questions(question_text_locator)  # получить текст вопроса
        # assert correct_text == text  # сравнить текст из переменной с эталоном
