from selenium.webdriver.common.by import By


class InventoryPageLocators:
    INVENTORY_ITEM_IMG = By.CLASS_NAME, "inventory_item_img"   # картинка
    INVENTORY_ITEM_TITLE = By.CLASS_NAME, "inventory_item_name"   # название
    INVENTORY_ITEM_PRICE = By.CLASS_NAME, "inventory_item_price"        # цена
    INVENTORY_ITEM_DESC = By.CLASS_NAME, "inventory_item_desc"         # описание
    ADD_TO_CART = By.ID, "add-to-cart-sauce-labs-backpack"
    REMOVE = By.ID, f"remove-sauce-labs-backpack"

    BASE_ADD_TO_CART_B = By.ID, f"add-to-cart-sauce-labs-backpack"
    SHOPPING_CART_ADD = By.CLASS_NAME, "shopping_cart_badge"

    SELECT_CONTAINER = By.CLASS_NAME, "product_sort_container"
    ACTIVE_OPTION = By.CLASS_NAME, "active_option"

    INVENTORY_DETAILS_IMG = By.CLASS_NAME, "inventory_details_img"
    INVENTORY_DETAILS_NAME = By.CLASS_NAME, "inventory_details_name large_size"
    INVENTORY_DETAILS_DESC = By.CLASS_NAME, "inventory_details_desc large_size"
    INVENTORY_DETAILS_PRICE = By.CLASS_NAME, "inventory_details_price"
