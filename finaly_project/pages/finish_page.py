from finaly_project.pages.main_page import MainPage
from finaly_project.locators.finish_page_locators import FinishPageLocators as FPL


class FinishPage(MainPage):

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser
        self.COMPLETE_TEXT_FIELD = self.browser.find_element(*FPL.COMPLETE_TEXT)
        self.COMPLETE_MESSAGE_FIELD = self.browser.find_element(*FPL.COMPLETE_MESSAGE)

    def home(self):
        return self.browser.find_element(*FPL.BACK_HOME)

    def complete_img(self):
        return self.browser.find_element(*FPL.COMPLETE)

    def complete_message(self):
        return self.COMPLETE_MESSAGE_FIELD.text

    def complete_text(self):
        return self.COMPLETE_TEXT_FIELD.text
