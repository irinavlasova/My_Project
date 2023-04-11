from finaly_project.pages.main_page import MainPage
from finaly_project.locators.checkout_step_one_locators import CheckoutPageLocators


class CheckoutPage(MainPage):

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser
        self.FIRST_NAME_FIELD = self.browser.find_element(*CheckoutPageLocators.FIRST_NAME)
        self.LAST_NAME_FIELD = self.browser.find_element(*CheckoutPageLocators.LAST_NAME)
        self.POSTAL_CODE_FIELD = self.browser.find_element(*CheckoutPageLocators.POSTAL_CODE)
        self.CONTINUE_FIELD = self.browser.find_element(*CheckoutPageLocators.CONTINUE)

    def cancel_button(self):
        return self.browser.find_element(*CheckoutPageLocators.CANCEL)

    def first_name_set(self, user_name):
        self.FIRST_NAME_FIELD.click()
        self.FIRST_NAME_FIELD.send_keys(user_name)

    def first_name_get(self):
        self.FIRST_NAME_FIELD.click()
        value = self.FIRST_NAME_FIELD.get_attribute("value")
        return value

    def last_name_set(self, user_last_name):
        self.LAST_NAME_FIELD.click()
        self.LAST_NAME_FIELD.send_keys(user_last_name)

    def last_name_get(self):
        self.LAST_NAME_FIELD.click()
        value = self.LAST_NAME_FIELD.get_attribute("value")
        return value

    def postal_code_set(self, post_cod):
        self.POSTAL_CODE_FIELD.click()
        self.POSTAL_CODE_FIELD.send_keys(post_cod)

    def postal_code_get(self):
        self.POSTAL_CODE_FIELD.click()
        value = self.POSTAL_CODE_FIELD.get_attribute("value")
        return value

    def continue_button(self):
        return self.CONTINUE_FIELD

    def checkout(self, user_name, user_last_name, post_cod):
        self.first_name_set(user_name)
        self.last_name_set(user_last_name)
        self.postal_code_set(post_cod)
