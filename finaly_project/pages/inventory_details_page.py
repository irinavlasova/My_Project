from finaly_project.pages.main_page import MainPage
from finaly_project.locators.inventory_details_locators import InventoryDetailsPageLocators as IDPL


class InventoryPageDetails(MainPage):
    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    def button_to_back(self):
        return self.browser.find_element(*IDPL.BUTTON_TO_BACK)

    def details_item_img(self):
        return self.browser.find_element(*IDPL.INVENTORY_DETAILS_IMG)

    def details_item_name(self):
        return self.browser.find_element(*IDPL.INVENTORY_DETAILS_NAME)

    def details_item_price(self):
        return self.browser.find_element(*IDPL.INVENTORY_DETAILS_PRICE)

    def details_item_description(self):
        return self.browser.find_element(*IDPL.INVENTORY_DETAILS_DESC)
