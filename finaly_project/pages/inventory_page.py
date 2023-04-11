from selenium.webdriver.common.by import By
from finaly_project.pages.main_page import MainPage
from finaly_project.locators.inventory_page_locators import InventoryPageLocators as IPL


class InventoryPage(MainPage):
    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser
        self.ITEM_DESC_FIELD = self.browser.find_element(*IPL.INVENTORY_ITEM_DESC)
        self.SELECT_CONTAINER_FIELD = self.browser.find_element(*IPL.SELECT_CONTAINER)
        self.ACTIVE_OPTION_FIELD = self.browser.find_element(*IPL.ACTIVE_OPTION)

    def inventory_item_img(self):
        return self.browser.find_element(*IPL.INVENTORY_ITEM_IMG)

    def inventory_item_name(self):
        return self.browser.find_element(*IPL.INVENTORY_ITEM_TITLE)

    def inventory_item_price(self):
        return self.browser.find_element(*IPL.INVENTORY_ITEM_PRICE)

    def inventory_item_description(self):
        return self.ITEM_DESC_FIELD

    def select_container(self):
        return self.browser.find_element(*IPL.ACTIVE_OPTION)


class InventoryPageSelect(MainPage):
    def __init__(self, browser, n):
        super().__init__(browser)
        self.browser = browser
        self.n = n
        self.SELECT_CONTAINER_FIELD = self.browser.find_element(*IPL.SELECT_CONTAINER)

    def add_to_cart_button(self):
        return self.browser.find_element(By.ID, f"add-to-cart-sauce-labs-{self.n}")

    def remove_button(self):
        add = self.add_to_cart_button()
        add.click()
        return self.browser.find_element(By.ID, f"remove-sauce-labs-{self.n}")

    def select_options(self):
        self.SELECT_CONTAINER_FIELD.click()
        self.browser.find_element(By.XPATH, f'// *[ @ id = "header_container"] / div[2] / div / span / select /'
                                            f' option[{self.n}]').click()
        return self.browser.find_element(*IPL.ACTIVE_OPTION)

    def item_link(self):
        return self.browser.find_element(By.ID, f"item_{self.n}_img_link")
