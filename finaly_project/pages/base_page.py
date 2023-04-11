from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from finaly_project.locators.base_page_locators import BasePageLocators as BPL
from finaly_project.pages.main_page import MainPage
from finaly_project.locators.inventory_page_locators import InventoryPageLocators as IPL


class BasePage(MainPage):

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser
        self.MENU = browser.find_element(*BPL.SIDE_MENU)
        self.SHOPPING = browser.find_element(*BPL.SHOPPING_CART)

    def logo_base_page(self):
        return self.browser.find_element(*BPL.LOGO)

    def get_title(self):
        return self.browser.find_element(*BPL.TITLE)

    def get_twitter(self):
        twitter = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(BPL().TWITTER))
        return twitter

    def get_facebook(self):
        facebook = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(BPL().FACEBOOK))
        return facebook

    def get_linkedin(self):
        linkedin = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(BPL().LINKEDIN))
        return linkedin

    def get_footer_copy(self):
        return self.browser.find_element(*BPL.FOOTER_COPY)

    def shopping_cart(self):
        return self.SHOPPING

    def add_to_shopping_cart(self):
        return self.browser.find_element(*IPL.ADD_TO_CART)

    def get_menu(self):
        return self.MENU

    def menu_close_menu(self):
        self.MENU.click()
        self.browser.find_element(*BPL.BUTTON_CLOSE_MENU)

    def menu_inventory(self):
        self.SHOPPING.click()
        self.browser.find_element(*BPL.SHOPPING_CART_MENU).click()
        return self.browser.find_element(*BPL.INVENTORY_SIDEBAR)

    def menu_about(self):
        self.MENU.click()
        return self.browser.find_element(*BPL.ABOUT_SIDEBAR)

    def menu_logout(self):
        self.MENU.click()
        return self.browser.find_element(*BPL.LOGOUT_SIDEBAR)

    def menu_reset(self):
        self.MENU.click()
        return self.browser.find_element(*BPL.RESET_SIDEBAR)
