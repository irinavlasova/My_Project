from finaly_project.configs.main_config import MainConfig


class ShoppingCartPageConfig(MainConfig):
    def __init__(self):
        super().__init__()
        self.URL_STEP_ONE = self.URL + "checkout-step-one.html"
        self.text_your_cart = 'Your Cart'
        self.text_qty = "QTY"
        self.text_description = 'Description'
