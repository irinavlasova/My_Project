from finaly_project.configs.main_config import MainConfig


class Checkout_Page_Config(MainConfig):
    def __init__(self):
        super().__init__()
        self.FIRST_NAME = "User"
        self.LAST_NAME = "Standard"
        self.POST_COD = "1234"
        self.URL_STEP_TWO = self.URL + "checkout-step-two.html"
        self.ERROR = "Error: First Name is required"
