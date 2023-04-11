import pytest
from selenium import webdriver
from finaly_project.configs.main_config import MainConfig
from finaly_project.configs.login_page_config import Login_Page_Config as LPC
from finaly_project.pages.login_page import LoginPage
from finaly_project.locators.base_page_locators import BasePageLocators as BPL
from finaly_project.locators.shopping_cart_locators import ShoppingCartPageLocators as SCPL
from finaly_project.pages.checkout_page import CheckoutPage as CP
from finaly_project.configs.checkout_config import Checkout_Page_Config as CPC
from finaly_project.pages.base_page import BasePage as BP
from selenium.webdriver.common.by import By
from finaly_project.locators.inventory_page_locators import InventoryPageLocators as IPL
from finaly_project.configs.inventory_config import Inventory_Page_Config as IPC
from finaly_project.configs.base_page_config import BasePageConfig as BPC
from finaly_project.configs.shoping_cart_config import ShoppingCartPageConfig as SCPC
from finaly_project.locators.step_two_locators import TwoPageLocators as TPL
from finaly_project.configs.step_two_page_config import Two_Page_Config as TSC


@pytest.fixture(scope='class')
def open_browser():
    browser = webdriver.Chrome("Users/maksim/Downloads/my_progect")
    browser.maximize_window()
    yield browser
    browser.quit()


@pytest.fixture
def get_website(open_browser):
    open_browser.get(MainConfig().URL)
    open_browser.implicitly_wait(30)

    return open_browser


@pytest.fixture(scope='class')
def get_website_base(open_browser):
    open_browser.get(MainConfig().URL)
    open_browser.implicitly_wait(30)
    LoginPage(open_browser).LOGIN_FIELD.click()
    LoginPage(open_browser).LOGIN_FIELD.send_keys("standard_user")
    LoginPage(open_browser).PASSWORD_FIELD.click()
    LoginPage(open_browser).PASSWORD_FIELD.send_keys("secret_sauce")
    LoginPage(open_browser).LOGIN_PRESS_FIELD.click()

    return open_browser


@pytest.fixture
def come_back(get_website_base):
    yield get_website_base
    get_website_base.get(LPC().URL_CURRENT)


@pytest.fixture
def refresh(get_website_base):
    yield get_website_base
    reset = BP(get_website_base).menu_reset()
    reset.click()
    get_website_base.refresh()


@pytest.fixture(scope="class")
def get_details_page(get_website_base):
    item4 = get_website_base.find_element(By.ID, f"item_4_img_link")
    item4.click()

    return get_website_base


@pytest.fixture
def come_back_to_details(get_website_base):
    yield get_website_base
    get_website_base.get(IPC().URL_ITEM + "4")


@pytest.fixture(scope="class")
def get_shopping_cart(get_website_base):
    get_website_base.find_element(*IPL.ADD_TO_CART).click()
    get_website_base.find_element(*BPL.SHOPPING_CART).click()

    yield get_website_base

    reset = BP(get_website_base).menu_reset()
    reset.click()
    get_website_base.refresh()


@pytest.fixture
def come_back_to_shopping_cart(get_website_base):
    yield get_website_base
    get_website_base.get(BPC().URL_SHOPPING_CART_PAGE)


@pytest.fixture(scope="class")
def get_check_page(get_shopping_cart):
    get_shopping_cart.find_element(*SCPL.CHECKOUT).click()
    yield get_shopping_cart
    get_shopping_cart.refresh()


@pytest.fixture
def come_back_to_checkout(get_website_base):
    yield get_website_base
    get_website_base.get(SCPC().URL_STEP_ONE)


@pytest.fixture(scope="class")
def get_two_step_page(get_check_page):
    CP(get_check_page).FIRST_NAME_FIELD.click()
    CP(get_check_page).FIRST_NAME_FIELD.send_keys("qwert")
    CP(get_check_page).LAST_NAME_FIELD.click()
    CP(get_check_page).LAST_NAME_FIELD.send_keys("qwert")
    CP(get_check_page).POSTAL_CODE_FIELD.click()
    CP(get_check_page).POSTAL_CODE_FIELD.send_keys("qwert")
    CP(get_check_page).CONTINUE_FIELD.click()

    return get_check_page


@pytest.fixture
def come_back_to_step_two(get_check_page):
    yield get_check_page
    get_check_page.get(CPC().URL_STEP_TWO)


@pytest.fixture(scope="class")
def get_finish_page(get_two_step_page):
    button = get_two_step_page.find_element(*TPL.FINISH)
    button.click()

    return get_two_step_page


@pytest.fixture
def come_back_to_finish(get_two_step_page):
    yield get_two_step_page
    get_two_step_page.get(TSC().URL_FINISH)
