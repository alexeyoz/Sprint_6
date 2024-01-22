from selenium.webdriver.common.by import By


class QuestionsLocators:
    QUESTION_1 = (By.ID, 'accordion__heading-0')  # кнопка с вопросом 1
    QUESTION_1_TEXT = (By.XPATH, '//*[@id="accordion__panel-0"]/p')  # текст для вопроса 1
    QUESTION_2 = (By.ID, 'accordion__heading-1')  # кнопка с вопросом 2
    QUESTION_2_TEXT = (By.XPATH, '//*[@id="accordion__panel-1"]/p')  # текст для вопроса 2
    QUESTION_3 = (By.ID, 'accordion__heading-2')  # кнопка с вопросом 3
    QUESTION_3_TEXT = (By.XPATH, '//*[@id="accordion__panel-2"]/p')  # текст для вопроса 3
    QUESTION_4 = (By.ID, 'accordion__heading-3')  # кнопка с вопросом 4
    QUESTION_4_TEXT = (By.XPATH, '//*[@id="accordion__panel-3"]/p')  # текст для вопроса 4
    QUESTION_5 = (By.ID, 'accordion__heading-4')  # кнопка с вопросом 5
    QUESTION_5_TEXT = (By.XPATH, '//*[@id="accordion__panel-4"]/p')  # текст для вопроса 5
    QUESTION_6 = (By.ID, 'accordion__heading-5')  # кнопка с вопросом 6
    QUESTION_6_TEXT = (By.XPATH, '//*[@id="accordion__panel-5"]/p')  # текст для вопроса 6
    QUESTION_7 = (By.ID, 'accordion__heading-6')  # кнопка с вопросом 7
    QUESTION_7_TEXT = (By.XPATH, '//*[@id="accordion__panel-6"]/p')  # текст для вопроса 7
    QUESTION_8 = (By.ID, 'accordion__heading-7')  # кнопка с вопросом 8
    QUESTION_8_TEXT = (By.XPATH, '//*[@id="accordion__panel-7"]/p')  # текст для вопроса 8


