import allure
from selenium.common import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from finaly_project.helpers.actual_window import actual_window
from finaly_project.pages.base_page import BasePage as BP
from finaly_project.locators.base_page_locators import *
from finaly_project.configs.base_page_config import BasePageConfig as BPC
from finaly_project.configs.main_config import MainConfig as MC
from finaly_project.locators.base_page_locators import BasePageLocators as BPL
from finaly_project.locators.inventory_page_locators import InventoryPageLocators as IPL


class TestBasePage:
    @allure.story("valid")
    def test_logo_base_page(self, get_website_base):
        assert BP(get_website_base).logo_base_page().text == BPC().text_logo

    @allure.story("not valid")
    def test_logo_base_page_negative(self, get_website_base):
        assert BP(get_website_base).logo_base_page().text == ""

    def test_get_title(self, get_website_base):
        assert BP(get_website_base).get_title().text == BPC().title_logo

    def test_get_title_negative(self, get_website_base):
        assert BP(get_website_base).get_title().text != ""

    @allure.story("valid test about")
    def test_get_footer_copy(self, get_website_base):
        with allure.step("step for getting test"):
            copy = BP(get_website_base).get_footer_copy()
            assert copy.text != BPC().text_copy

    def test_get_footer_copy_negative(self, get_website_base):
        copy = BP(get_website_base).get_footer_copy()
        assert copy.text != ""

    def test_get_menu(self, get_website_base, come_back):
        menu = BP(get_website_base).get_menu()
        menu.click()
        get_website_base.find_element(*BPL.ABOUT_SIDEBAR).click()

        assert get_website_base.current_url == BPC().URL_CURRENT_BASE_MENU

    def test_menu_negative(self, get_website_base, come_back):
        menu_item = WebDriverWait(get_website_base, 10).until(
            EC.presence_of_element_located(BPL.ABOUT_SIDEBAR))

        assert not menu_item.is_displayed()

    def test_close_menu(self, get_website_base, come_back):
        menu_item = WebDriverWait(get_website_base, 10).until(
            EC.presence_of_element_located(BPL.ABOUT_SIDEBAR))

        assert not menu_item.is_displayed()

    def test_close_menu_negative(self, get_website_base, come_back):
        BP(get_website_base).menu_close_menu()
        get_website_base.find_element(*BPL.ABOUT_SIDEBAR).click()

        assert get_website_base.current_url == BPC().URL_CURRENT_BASE_MENU

    def test_menu_inventory(self, get_website_base, come_back):
        inventory = BP(get_website_base).menu_inventory()
        inventory.click()

        assert get_website_base.current_url == BPC().URL_CURRENT_BASE

    def test_menu_inventory_negative(self, get_website_base, come_back):
        BP(get_website_base).menu_inventory()

        assert get_website_base.current_url == BPC().URL_SHOPPING_CART_PAGE

    def test_menu_about(self, get_website_base, come_back):
        about = BP(get_website_base).menu_about()
        about.click()

        assert get_website_base.current_url == BPC().URL_CURRENT_BASE_MENU

    def test_menu_about_negative(self, get_website_base, come_back):
        BP(get_website_base).menu_about()

        assert get_website_base.current_url == BPC().URL_CURRENT_BASE

    def test_menu_logout_negative(self, get_website_base, come_back):
        BP(get_website_base).menu_logout()

        assert get_website_base.current_url == BPC().URL_CURRENT_BASE

    def test_menu_reset(self, get_website_base, come_back):
        get_website_base.find_element(*IPL().BASE_ADD_TO_CART_B).click()
        reset = BP(get_website_base).menu_reset()
        reset.click()
        get_website_base.find_element(By.CLASS_NAME, "shopping_cart_link")

        assert NoSuchElementException

    def test_menu_reset_negative(self, get_website_base, come_back):
        reset = BP(get_website_base).menu_reset()
        reset.click()
        get_website_base.find_element(*IPL().BASE_ADD_TO_CART_B).click()

        assert get_website_base.find_element(By.CLASS_NAME, "shopping_cart_link")

    def test_shopping_cart(self, get_website_base, come_back, refresh):
        shopping = BP(get_website_base).shopping_cart()
        shopping.click()

        assert get_website_base.current_url == BPC().URL_SHOPPING_CART_PAGE

    def test_add_to_shopping_cart(self, get_website_base, refresh):
        add_itme = BP(get_website_base).add_to_shopping_cart()
        add_itme.click()
        assert get_website_base.find_element(*IPL.SHOPPING_CART_ADD)

    def test_get_twitter(self, get_website_base, come_back):
        twitter = BP(get_website_base).get_twitter()
        twitter.click()
        actual_window(get_website_base)

        assert get_website_base.current_url == BPC().URL_TWITTER

    def test_get_facebook(self, get_website_base, come_back):
        facebook = BP(get_website_base).get_facebook()
        facebook.click()
        actual_window(get_website_base)

        assert get_website_base.current_url == BPC().URL_facebook

    def test_get_linkedin(self, get_website_base, come_back):
        linkedin = BP(get_website_base).get_linkedin()
        linkedin.click()
        actual_window(get_website_base)

        assert get_website_base.current_url == BPC().URL_linkedin or BPC().URL_linkedin_two

    def test_get_twitter_negative(self, get_website_base, come_back):
        twitter = BP(get_website_base).get_twitter()
        twitter.click()

        assert get_website_base.current_url == BPC().URL_CURRENT_BASE

    def test_get_facebook_negative(self, get_website_base, come_back):
        facebook = BP(get_website_base).get_facebook()
        facebook.click()

        assert get_website_base.current_url == BPC().URL_CURRENT_BASE

    def test_get_linkedin_negative(self, get_website_base, come_back):
        linkedin = BP(get_website_base).get_linkedin()
        linkedin.click()

        assert get_website_base.current_url == BPC().URL_CURRENT_BASE

    def test_menu_logout(self, get_website_base):
        logout = BP(get_website_base).menu_logout()
        logout.click()

        assert get_website_base.current_url == MC().URL
