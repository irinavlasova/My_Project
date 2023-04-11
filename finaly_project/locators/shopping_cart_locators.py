from selenium.webdriver.common. by import By


class ShoppingCartPageLocators:

    TITLE_SHOPPING_CART = By.CLASS_NAME, "title"
    QTY = By.CLASS_NAME, "cart_quantity_label"
    SHOPPING_DESCRIPTION = By.CLASS_NAME, "cart_desc_label"
    CONTINUE_SHOPPING = By.ID, "continue-shopping"
    CHECKOUT = By.ID, "checkout"
    CART_ITEM = By.CLASS_NAME, "cart_item"

    CART_QUANTITY = By.CLASS_NAME, "cart_quantity"
    INVENTORY_ITEM_NAME = By.CLASS_NAME, "inventory_item_name"
    INVENTORY_ITEM_DESC = By.CLASS_NAME, "inventory_item_desc"
    INVENTORY_ITEM_PRICE = By.CLASS_NAME, "inventory_item_price"
    REMOVE = By.ID, "remove-sauce-labs-backpack"
