from finaly_project.configs.base_page_config import BasePageConfig as BPC
from finaly_project.configs.step_two_page_config import Two_Page_Config as TSC
from finaly_project.pages.step_two_page import Two_Step_Page as TSP
from finaly_project.configs.checkout_config import Checkout_Page_Config as CPC
from finaly_project.configs.shoping_cart_config import ShoppingCartPageConfig as SCPC


class TestTwoStepPage:
    def test_cart_quantity_label(self, get_two_step_page):
        qty = TSP(get_two_step_page).qty()
        assert qty.text == SCPC().text_qty

    def test_cart_quantity_label_negative(self, get_two_step_page):
        qty = TSP(get_two_step_page).qty()
        assert qty.text == SCPC().text_qty != ""

    def test_cart_desc_label(self, get_two_step_page):
        description = TSP(get_two_step_page).description()
        assert description.text == SCPC().text_description

    def test_cart_desc_label_negative(self, get_two_step_page):
        description = TSP(get_two_step_page).description()
        assert description.text != ""

    def test_info_payment(self, get_two_step_page):
        payment = TSP(get_two_step_page).info_payment()
        assert payment.text == TSC().PAYMENT

    def test_info_payment_negative(self, get_two_step_page):
        payment = TSP(get_two_step_page).info_payment()
        assert payment.text != ""

    def test_shopping_info(self, get_two_step_page):
        shopping = TSP(get_two_step_page).shopping_info()
        assert shopping.text == TSC().INFO_SHOP

    def test_shopping_info_negative(self, get_two_step_page):
        shopping = TSP(get_two_step_page).shopping_info()
        assert shopping.text != ""

    def test_price_total(self, get_two_step_page):
        total = TSP(get_two_step_page).price_total()
        assert total.text == TSC().TOTAL

    def test_price_total_negative(self, get_two_step_page):
        total = TSP(get_two_step_page).price_total()
        assert total.text != ""

    def test_sauce_card(self, get_two_step_page):
        sauce_card = TSP(get_two_step_page).sauce_card()
        assert sauce_card.text == TSC().SAUCE_CARD

    def test_sauce_card_negative(self, get_two_step_page):
        sauce_card = TSP(get_two_step_page).sauce_card()
        assert sauce_card.text != ''

    def test_delivery(self, get_two_step_page):
        delivery = TSP(get_two_step_page).delivery()
        assert delivery.text == TSC().INFO_DELIVERY

    def test_delivery_negative(self, get_two_step_page):
        delivery = TSP(get_two_step_page).delivery()
        assert delivery.text != ''

    def test_item_total(self, get_two_step_page):
        item_total = TSP(get_two_step_page).item_total()
        assert item_total.text == TSC().INFO_ITEM_TOTAL

    def test_item_total_negative(self, get_two_step_page):
        item_total = TSP(get_two_step_page).item_total()
        assert item_total.text != ''

    def test_tax(self, get_two_step_page):
        tax = TSP(get_two_step_page).tax()
        assert tax.text == TSC().INFO_TAX

    def test_tax_negative(self, get_two_step_page):
        tax = TSP(get_two_step_page).tax()
        assert tax.text != ''

    def test_total(self, get_two_step_page):
        total = TSP(get_two_step_page).total()
        assert total.text == TSC().INFO_TOTAL_PRICE

    def test_total_negative(self, get_two_step_page):
        total = TSP(get_two_step_page).total()
        assert total.text != ''

    def test_finish_button(self, get_two_step_page, come_back_to_step_two):
        button = TSP(get_two_step_page).finish_button()
        button.click()
        assert get_two_step_page.current_url == TSC().URL_FINISH

    def test_finish_button_negative(self, get_two_step_page, come_back_to_step_two):
        TSP(get_two_step_page).finish_button()
        assert get_two_step_page.current_url == CPC().URL_STEP_TWO

    def test_cancel_button(self, get_two_step_page, come_back_to_step_two):
        button = TSP(get_two_step_page).cancel_button()
        button.click()
        assert get_two_step_page.current_url == BPC().URL_CURRENT_BASE

    def test_cancel_button_negative(self, get_two_step_page, come_back_to_step_two):
        TSP(get_two_step_page).cancel_button()
        assert get_two_step_page.current_url == CPC().URL_STEP_TWO
