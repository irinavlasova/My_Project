from selenium.common import NoSuchElementException
from finaly_project.locators.shopping_cart_locators import ShoppingCartPageLocators as SCPL
from finaly_project.pages.shopping_cart_page import ShoppingCartPage as SP
from finaly_project.configs.shoping_cart_config import ShoppingCartPageConfig as SPC
from finaly_project.configs.base_page_config import BasePageConfig as BPC
from finaly_project.configs.inventory_details_config import InventoryPageDetailsConfig as IPDC
from finaly_project.configs.inventory_config import Inventory_Page_Config as IPC
from finaly_project.configs.shoping_cart_config import ShoppingCartPageConfig as SCPC


class TestShoppingCartPage:
    def test_cart_contents_container(self, get_shopping_cart):
        title = SP(get_shopping_cart).title_page()
        assert title.text == SCPC().text_your_cart

    def test_cart_contents_container_negative(self, get_shopping_cart):
        title = SP(get_shopping_cart).title_page()
        assert title.text != ''

    def test_cart_quantity_label(self, get_shopping_cart):
        qty = SP(get_shopping_cart).cart_quantity_label()
        assert qty.text == SCPC().text_qty

    def test_cart_quantity_label_negative(self, get_shopping_cart):
        qty = SP(get_shopping_cart).cart_quantity_label()
        assert qty.text != ""

    def test_cart_desc_label(self, get_shopping_cart):
        description = SP(get_shopping_cart).cart_desc_label()
        assert description.text == SCPC().text_description

    def test_cart_desc_label_negative(self, get_shopping_cart):
        description = SP(get_shopping_cart).cart_desc_label()
        assert description.text != ""

    def test_continue_shopping_button(self, get_shopping_cart, come_back_to_shopping_cart):
        continue_button = SP(get_shopping_cart).continue_shopping_button()
        continue_button.click()
        assert get_shopping_cart.current_url == BPC().URL_CURRENT_BASE

    def test_continue_shopping_button_negative(self, get_shopping_cart):
        SP(get_shopping_cart).continue_shopping_button()
        assert get_shopping_cart.current_url == BPC().URL_SHOPPING_CART_PAGE

    def test_checkout_button(self, get_shopping_cart, come_back_to_shopping_cart):
        checkout_button = SP(get_shopping_cart).checkout_button()
        checkout_button.click()
        assert get_shopping_cart.current_url == SPC().URL_STEP_ONE

    def test_checkout_button_negative(self, get_shopping_cart):
        SP(get_shopping_cart).checkout_button()
        assert get_shopping_cart.current_url == BPC().URL_SHOPPING_CART_PAGE

    def test_cart_quantity(self, get_shopping_cart):
        quantity = SP(get_shopping_cart).cart_quantity()
        assert quantity.text == "1"

    def test_cart_quantity_negative(self, get_shopping_cart):
        quantity = SP(get_shopping_cart).cart_quantity()
        assert quantity.text != ''

    def test_inventory_item_name(self, get_shopping_cart):
        name = SP(get_shopping_cart).inventory_item_name()
        assert name.text == IPDC().name_4

    def test_inventory_item_name_negative(self, get_shopping_cart):
        name = SP(get_shopping_cart).inventory_item_name()
        assert name.text != ''

    def test_inventory_item_desc(self, get_shopping_cart):
        description = SP(get_shopping_cart).inventory_item_desc()
        assert description.text == IPDC().description

    def test_inventory_item_desc_negative(self, get_shopping_cart):
        description = SP(get_shopping_cart).inventory_item_desc()
        assert description.text != ''

    def test_inventory_item_price(self, get_shopping_cart):
        assert SP(get_shopping_cart).inventory_item_price().text == IPC().PRICE

    def test_inventory_item_price_negative(self, get_shopping_cart):
        assert SP(get_shopping_cart).inventory_item_price().text != ''

    def test_remove_item_negative(self, get_shopping_cart):
        SP(get_shopping_cart).remove_item()
        assert get_shopping_cart.find_element(*SCPL.CART_ITEM)

    def test_remove_item(self, get_shopping_cart):
        button = SP(get_shopping_cart).remove_item()
        button.click()
        try:
            get_shopping_cart.find_element(*SCPL.CART_ITEM)
        except NoSuchElementException:
            return False, print("False")
        return True, print("True")
