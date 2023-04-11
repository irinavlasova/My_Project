from finaly_project.pages.main_page import MainPage
from finaly_project.locators.step_two_locators import TwoPageLocators as TPL


class Two_Step_Page(MainPage):
    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    def finish_button(self):
        return self.browser.find_element(*TPL.FINISH)

    def cancel_button(self):
        return self.browser.find_element(*TPL.CANCEL)

    def qty(self):
        return self.browser.find_element(*TPL.QTY)

    def description(self):
        return self.browser.find_element(*TPL.DESCRIPTION)

    def info_payment(self):
        return self.browser.find_element(*TPL.PAYMENT_INF)

    def shopping_info(self):
        return self.browser.find_element(*TPL.SHOPPING_INF)

    def price_total(self):
        return self.browser.find_element(*TPL.PRICE_TOTAL)

    def sauce_card(self):
        return self.browser.find_element(*TPL.SAUCECARD)

    def delivery(self):
        return self.browser.find_element(*TPL.DELIVERY)

    def item_total(self):
        return self.browser.find_element(*TPL.ITEM_TOTAL)

    def tax(self):
        return self.browser.find_element(*TPL.TAX)

    def total(self):
        return self.browser.find_element(*TPL.TOTAL)
