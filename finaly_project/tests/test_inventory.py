from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from finaly_project.locators.inventory_page_locators import InventoryPageLocators as IPL
from finaly_project.pages.inventory_page import InventoryPage as IP
from finaly_project.pages.inventory_page import InventoryPageSelect as IPS
from finaly_project.configs.inventory_config import Inventory_Page_Config as IPC
from finaly_project.configs.base_page_config import BasePageConfig as BPC
from finaly_project.configs.inventory_details_config import InventoryPageDetailsConfig as IPDC
from selenium.common.exceptions import NoSuchElementException


class TestInventoryPage:
    def test_inventory_item_img(self, get_website_base, come_back):
        img = IP(get_website_base).inventory_item_img()
        img.click()
        assert get_website_base.current_url == IPC().URL_ITEM + "4"

    def test_inventory_item_img_negative(self, get_website_base):
        IP(get_website_base).inventory_item_img()
        assert get_website_base.current_url == BPC().URL_CURRENT_BASE

    def test_inventory_item_name(self, get_website_base, come_back):
        name = IP(get_website_base).inventory_item_name()
        name.click()
        assert get_website_base.current_url == IPC().URL_ITEM + "4"

    def test_inventory_item_name_negative(self, get_website_base):
        IP(get_website_base).inventory_item_name()
        assert get_website_base.current_url == BPC().URL_CURRENT_BASE

    def test_inventory_item_price(self, get_website_base):
        assert IP(get_website_base).inventory_item_price().text == "$29.99"

    def test_inventory_item_price_negative(self, get_website_base):
        assert IP(get_website_base).inventory_item_price().text != ""

    def test_inventory_item_description(self, get_website_base):
        description = IP(get_website_base).inventory_item_description()
        assert description.text == IPDC().description

    def test_inventory_item_description_negative(self, get_website_base):
        description = IP(get_website_base).inventory_item_description()
        assert description.text != ""

    def test_add_to_cart_button(self, get_website_base, come_back, refresh):
        item_4 = IPS(get_website_base, "backpack").add_to_cart_button()
        item_4.click()
        assert get_website_base.find_element(*IPL.SHOPPING_CART_ADD)
        assert get_website_base.find_element(*IPL.REMOVE)

    def test_add_to_cart_button_negative(self, get_website_base):
        try:
            get_website_base.find_element(*IPL.REMOVE)
        except NoSuchElementException:
            return False, print("False")
        return True, print("True")

    def test_remove_button(self, get_website_base, refresh):
        a = IPS(get_website_base, "backpack").remove_button()
        a.click()

        assert get_website_base.find_element(*IPL.ADD_TO_CART)

    def test_remove_button_negative(self, get_website_base):
        IPS(get_website_base, "backpack").remove_button()
        try:
            get_website_base.find_element(*IPL.ADD_TO_CART)
        except NoSuchElementException:
            return False, print("False")
        return True, print("True")

    def test_select_container(self, get_website_base):
        az = IP(get_website_base).select_container()

        assert az.text == "Name (A to Z)"

    def test_select_container_negative(self, get_website_base):
        az = IP(get_website_base).select_container()

        assert az.text != ""

    def test_select_options(self, get_website_base):
        select_az = IPS(get_website_base, 1).select_options()

        assert select_az.text == "Name (A to Z)"

    def test_select_options_negative(self, get_website_base):
        select_az = IPS(get_website_base, 1).select_options()

        assert select_az.text != ""

    def test_select_container_za(self, get_website_base):
        select_za = IPS(get_website_base, "2").select_options()

        assert select_za.text == "Name (Z to A)"

    def test_select_container_za_negative(self, get_website_base):
        select_za = IPS(get_website_base, "2").select_options()

        assert select_za.text != ""

    def test_select_container_lohi(self, get_website_base):
        select_lohi = IPS(get_website_base, "3").select_options()

        assert select_lohi.text == "Price (low to high)"

    def test_select_container_lohi_negative(self, get_website_base):
        select_lohi = IPS(get_website_base, "3").select_options()

        assert select_lohi.text != ""

    def test_select_container_hilo(self, get_website_base):
        select_hilo = IPS(get_website_base, "4").select_options()

        assert select_hilo.text == "Price (high to low)"

    def test_select_container_hilo_negative(self, get_website_base):
        select_hilo = IPS(get_website_base, "4").select_options()

        assert select_hilo.text != ""

    def test_item_1(self, get_website_base, come_back):
        item_1 = IPS(get_website_base, 1).item_link()
        item_1.click()
        assert get_website_base.current_url == IPC().URL_ITEM + "1"

    def test_item_1_negative(self, get_website_base):
        IPS(get_website_base, 1).item_link()
        assert get_website_base.current_url == BPC().URL_CURRENT_BASE

    def test_item_2(self, get_website_base, come_back):
        item_2 = IPS(get_website_base, 2).item_link()
        item_2.click()
        assert get_website_base.current_url == IPC().URL_ITEM + "2"

    def test_item_2_negative(self, get_website_base):
        IPS(get_website_base, 2).item_link()
        assert get_website_base.current_url == BPC().URL_CURRENT_BASE

    def test_item_3(self, get_website_base, come_back):
        item_3 = IPS(get_website_base, 3).item_link()
        item_3.click()
        assert get_website_base.current_url == IPC().URL_ITEM + "3"

    def test_item_3_negative(self, get_website_base):
        IPS(get_website_base, 3).item_link()
        assert get_website_base.current_url == BPC().URL_CURRENT_BASE

    def test_item_4(self, get_website_base, come_back):
        item_4 = IPS(get_website_base, 4).item_link()
        item_4.click()
        assert get_website_base.current_url == IPC().URL_ITEM + "4"

    def test_item_4_negative(self, get_website_base):
        IPS(get_website_base, 4).item_link()
        assert get_website_base.current_url == BPC().URL_CURRENT_BASE

    def test_item_5(self, get_website_base, come_back):
        item_5 = IPS(get_website_base, 5).item_link()
        item_5.click()
        assert get_website_base.current_url == IPC().URL_ITEM + "5"

    def test_item_5_negative(self, get_website_base):
        IPS(get_website_base, 5).item_link()
        assert get_website_base.current_url == BPC().URL_CURRENT_BASE
