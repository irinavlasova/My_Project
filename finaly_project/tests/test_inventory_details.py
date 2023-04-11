from finaly_project.configs.inventory_details_config import InventoryPageDetailsConfig as IPDC
from finaly_project.pages.inventory_details_page import InventoryPageDetails as IPD
from finaly_project.configs.inventory_config import Inventory_Page_Config as IPC
from finaly_project.helpers.actual_window import actual_window
from finaly_project.configs.base_page_config import BasePageConfig as BPC


class TestInventoryDetailsPage:
    def test_details_item_img(self, get_details_page):
        IPD(get_details_page).details_item_img()
        assert get_details_page.current_url == IPC().URL_ITEM + "4"

    def test_details_item_price(self, get_details_page):
        assert IPD(get_details_page).details_item_price().text == IPC().PRICE

    def test_details_item_price_negative(self, get_details_page):
        assert IPD(get_details_page).details_item_price().text != ''

    def test_details_item_name(self, get_details_page):
        name = IPD(get_details_page).details_item_name()
        assert name.text == IPDC().name_4

    def test_details_item_name_negative(self, get_details_page):
        name = IPD(get_details_page).details_item_name()

        assert name.text != ''

    def test_details_item_description(self, get_details_page):
        description = IPD(get_details_page).details_item_description()
        assert description.text == IPDC().description

    def test_details_item_description_negative(self, get_details_page):
        description = IPD(get_details_page).details_item_description()
        assert description.text != ''

    def test_button_to_back(self, get_details_page, come_back_to_details):
        button = IPD(get_details_page).button_to_back()
        button.click()
        actual_window(get_details_page)
        assert get_details_page.current_url == BPC().URL_CURRENT_BASE

    def test_button_to_back_negative(self, get_details_page):
        IPD(get_details_page).button_to_back()
        assert get_details_page.current_url == IPC().URL_ITEM + "4"
