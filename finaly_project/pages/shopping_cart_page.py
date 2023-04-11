from finaly_project.pages.main_page import MainPage
from finaly_project.locators.shopping_cart_locators import ShoppingCartPageLocators


class ShoppingCartPage(MainPage):

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    def title_page(self):
        return self.browser.find_element(*ShoppingCartPageLocators.TITLE_SHOPPING_CART)

    def cart_quantity_label(self):
        return self.browser.find_element(*ShoppingCartPageLocators.QTY)

    def cart_desc_label(self):
        return self.browser.find_element(*ShoppingCartPageLocators.SHOPPING_DESCRIPTION)

    def continue_shopping_button(self):
        return self.browser.find_element(*ShoppingCartPageLocators.CONTINUE_SHOPPING)

    def checkout_button(self):
        return self.browser.find_element(*ShoppingCartPageLocators.CHECKOUT)

    def cart_quantity(self):
        return self.browser.find_element(*ShoppingCartPageLocators.CART_QUANTITY)

    def inventory_item_name(self):
        return self.browser.find_element(*ShoppingCartPageLocators.INVENTORY_ITEM_NAME)

    def inventory_item_desc(self):
        return self.browser.find_element(*ShoppingCartPageLocators.INVENTORY_ITEM_DESC)

    def inventory_item_price(self):
        return self.browser.find_element(*ShoppingCartPageLocators.INVENTORY_ITEM_PRICE)

    def remove_item(self):
        return self.browser.find_element(*ShoppingCartPageLocators.REMOVE)
