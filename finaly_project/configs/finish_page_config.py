from finaly_project.configs.main_config import MainConfig


class Finish_Page_Config(MainConfig):
    def __init__(self):
        super().__init__()
        self.FINISH_COMPLETE_TEXT = "Your order has been dispatched, and will arrive just as fast as the pony can " \
                                    "get there!"
        self.FINISH_COMPLETE_MESSAGE = "Thank you for your order!"
