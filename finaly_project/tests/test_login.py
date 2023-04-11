from finaly_project.pages.login_page import LoginPage
from finaly_project.locators.login_page_locators import *
from finaly_project.configs.login_page_config import Login_Page_Config as LPC
from finaly_project.helpers.randomizer import *


class TestLogin:
    def test_login(self, get_website):
        LoginPage(get_website).login(LPC().USER_NAME, LPC().PASSWORD_USER)

        assert get_website.current_url == LPC().URL_CURRENT

    def test_login_negative(self, get_website):
        LoginPage(get_website).login(random_str(15), random_str(12))

        assert get_website.current_url != LPC().URL_CURRENT

    def test_login_set(self, get_website):
        LoginPage(get_website).login_set(LPC().USER_NAME)

        assert LoginPage(get_website).login_get() == LPC().USER_NAME

    def test_login_set_negative(self, get_website):
        LoginPage(get_website).login_set(random_str(15))

        assert LoginPage(get_website).login_get() != LPC().USER_NAME

    def test_login_get(self, get_website):
        assert LoginPage(get_website).login_get() == ""

    def test_login_get_negative(self, get_website):
        assert LoginPage(get_website).login_get() != int

    def test_password_set(self, get_website):
        LoginPage(get_website).password_set(LPC().PASSWORD_USER)

        assert LoginPage(get_website).password_get() == LPC().PASSWORD_USER

    def test_password_set_negative(self, get_website):
        LoginPage(get_website).password_set(random_str(12))

        assert LoginPage(get_website).password_get() != LPC().PASSWORD_USER

    def test_password_get(self, get_website):
        LoginPage(get_website).password_get()

        assert LoginPage(get_website).login_get() == ""

    def test_password_get_negative(self, get_website):
        LoginPage(get_website).password_get()

        assert LoginPage(get_website).login_get() != int

    def test_login_press(self, get_website):
        LoginPage(get_website).login_press()
        error = get_website.find_element(*LoginPageLocators.LOGIN_CONTAINER)
        assert error.text == LPC().error_text
