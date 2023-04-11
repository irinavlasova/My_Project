from finaly_project.configs.main_config import MainConfig


class Two_Page_Config(MainConfig):
    def __init__(self):
        super().__init__()
        self.URL_FINISH = self.URL + "checkout-complete.html"
        self.PAYMENT = "Payment Information"
        self.INFO_SHOP = "Shipping Information"
        self.TOTAL = "Price Total"
        self.SAUCE_CARD = 'SauceCard #31337'
        self.INFO_DELIVERY = 'Free Pony Express Delivery!'
        self.INFO_ITEM_TOTAL = "Item total: $29.99"
        self.INFO_TAX = 'Tax: $2.40'
        self.INFO_TOTAL_PRICE = 'Total: $32.39'
