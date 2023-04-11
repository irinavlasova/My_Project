from finaly_project.configs.main_config import MainConfig


class Inventory_Page_Config(MainConfig):
    def __init__(self):
        super().__init__()
        self.URL_ITEM = self.URL + "inventory-item.html?id="
        self.ITEM_4 = "backpack"
        self.PRICE = "$29.99"
