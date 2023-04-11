from finaly_project.pages.checkout_page import CheckoutPage as CP
from finaly_project.configs.checkout_config import Checkout_Page_Config as CPC
from finaly_project.configs.base_page_config import BasePageConfig as BPC
from finaly_project.locators.checkout_step_one_locators import CheckoutPageLocators as CPL
from finaly_project.configs.shoping_cart_config import ShoppingCartPageConfig as SCPC


class TestCheckoutPage:
    def test_cancel_button(self, get_check_page, come_back_to_checkout):
        button = CP(get_check_page).cancel_button()
        button.click()
        assert get_check_page.current_url == BPC().URL_SHOPPING_CART_PAGE

    def test_cancel_button_negative(self, get_check_page):
        CP(get_check_page).cancel_button()
        assert get_check_page.current_url == SCPC().URL_STEP_ONE

    def test_first_name_set(self, get_check_page):
        CP(get_check_page).first_name_set(CPC().FIRST_NAME)

        assert CP(get_check_page).first_name_get() == CPC().FIRST_NAME

    def test_first_name_set_negative(self, get_check_page):
        CP(get_check_page).first_name_set(CPC().FIRST_NAME)

        assert CP(get_check_page).first_name_get() != ''

    def test_first_name_get(self, get_check_page):
        assert CP(get_check_page).first_name_get() != str

    def test_first_name_get_negative(self, get_check_page):
        assert CP(get_check_page).first_name_get() != int

    def test_last_name_set(self, get_check_page):
        CP(get_check_page).last_name_set(CPC().LAST_NAME)

        assert CP(get_check_page).last_name_get() == CPC().LAST_NAME

    def test_last_name_set_negative(self, get_check_page):
        CP(get_check_page).last_name_set(CPC().LAST_NAME)

        assert CP(get_check_page).last_name_get() != ''

    def test_last_name_get(self, get_check_page):
        assert CP(get_check_page).last_name_get() != str

    def test_last_name_get_negative(self, get_check_page):
        assert CP(get_check_page).last_name_get() != int

    def test_postal_code_set(self, get_check_page):
        CP(get_check_page).postal_code_set(CPC().POST_COD)

        assert CP(get_check_page).postal_code_get() == CPC().POST_COD

    def test_postal_code_set_negative(self, get_check_page):
        CP(get_check_page).postal_code_set(CPC().POST_COD)

        assert CP(get_check_page).postal_code_get() != ''

    def test_postal_code_get(self, get_check_page):
        assert CP(get_check_page).postal_code_get() != str

    def test_postal_code_get_negative(self, get_check_page):
        assert CP(get_check_page).postal_code_get() != int

    def test_checkout(self, get_check_page, come_back_to_checkout):
        CP(get_check_page).checkout(CPC().FIRST_NAME, CPC().LAST_NAME, CPC().POST_COD)
        button = CP(get_check_page).continue_button()
        button.click()

        assert get_check_page.current_url == CPC().URL_STEP_TWO

    def test_checkout_negative(self, get_check_page,  come_back_to_checkout):
        CP(get_check_page).checkout(CPC().FIRST_NAME, CPC().LAST_NAME, CPC().POST_COD)
        CP(get_check_page).continue_button()

        assert get_check_page.current_url == SCPC().URL_STEP_ONE

    def test_continue_button(self, get_check_page, come_back_to_checkout):
        click_button = CP(get_check_page).continue_button()
        click_button.click()
        error = get_check_page.find_element(*CPL.ERROR)

        assert error.text == CPC().ERROR

    def test_continue_button_negative(self, get_check_page):
        click_button = CP(get_check_page).continue_button()
        click_button.click()
        error = get_check_page.find_element(*CPL.ERROR)

        assert error.text != ""
