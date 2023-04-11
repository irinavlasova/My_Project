from finaly_project.pages.main_page import MainPage
from finaly_project.locators.login_page_locators import LoginPageLocators


class LoginPage(MainPage):

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser
        self.LOGIN_FIELD = browser.find_element(*LoginPageLocators.LOGIN)
        self.PASSWORD_FIELD = browser.find_element(*LoginPageLocators.PASSWORD)
        self.LOGIN_PRESS_FIELD = browser.find_element(*LoginPageLocators.LOGIN_BUTTON)

    def login_set(self, user):
        self.LOGIN_FIELD.click()
        self.LOGIN_FIELD.send_keys(user)

    def login_get(self):
        self.LOGIN_FIELD.click()
        value = self.LOGIN_FIELD.get_attribute("value")
        return value

    def password_set(self, password):
        self.PASSWORD_FIELD.click()
        self.PASSWORD_FIELD.send_keys(password)

    def password_get(self):
        self.PASSWORD_FIELD.click()
        value = self.PASSWORD_FIELD.get_attribute("value")
        return value

    def login_press(self):
        self.LOGIN_PRESS_FIELD.click()

    def login_get_text(self):
        self.LOGIN_PRESS_FIELD.click()
        self.LOGIN_PRESS_FIELD.text()

    # def login_empty_button(self):
    #     self.LOGIN_PRESS_FIELD.click()
    #     return self.browser.find_element(LoginPageLocators().LOGIN_BUTTON_FAIL)

    def login(self, user, password):
        self.login_set(user)
        self.password_set(password)
        self.login_press()

    def logo(self):
        self.browser.find_element(*LoginPageLocators.LOGO)
