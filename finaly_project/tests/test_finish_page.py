from finaly_project.pages.finish_page import FinishPage as FP
from finaly_project.configs.base_page_config import BasePageConfig as BPC
from finaly_project.locators.finish_page_locators import FinishPageLocators as FPL
from finaly_project.configs.finish_page_config import Finish_Page_Config as FPC
from finaly_project.configs.step_two_page_config import Two_Page_Config as TPC


class TestFinishPage:
    def test_home_button(self, get_finish_page, come_back_to_finish):
        button = FP(get_finish_page).home()
        button.click()
        assert get_finish_page.current_url == BPC().URL_CURRENT_BASE

    def test_home_button_negative(self, get_finish_page):
        FP(get_finish_page).home()
        assert get_finish_page.current_url == TPC().URL_FINISH

    def test_complete_message(self, get_finish_page):
        assert FP(get_finish_page).complete_message() == FPC().FINISH_COMPLETE_MESSAGE

    def test_complete_message_negative(self, get_finish_page):
        assert FP(get_finish_page).complete_message() != ''

    def test_complete_text(self, get_finish_page):
        assert FP(get_finish_page).complete_text() == FPC().FINISH_COMPLETE_TEXT

    def test_complete_text_negative(self, get_finish_page):
        assert FP(get_finish_page).complete_text() != ''

    def test_complete_img(self, get_finish_page):
        assert FP(get_finish_page).complete_img() == get_finish_page.find_element(*FPL.COMPLETE)
