import allure

from pages.base_page import BasePage


class QuestionsPage(BasePage):
    @allure.step("Проверка текста при клике на вопрос о важном ")
    def check_the_questions(self, question_locator, question_text_locator):
        self.find_element_located_click(question_locator)
        self.find_element_located_click(question_locator)
        text_questions = self.find_element_located(question_text_locator).text
        return text_questions




