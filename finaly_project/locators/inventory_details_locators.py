from selenium.webdriver.common.by import By


class InventoryDetailsPageLocators:
    BUTTON_TO_BACK = By.ID, "back-to-products"
    INVENTORY_DETAILS_IMG = By.CLASS_NAME, "inventory_details_img"
    INVENTORY_DETAILS_NAME = By.XPATH, '//*[@id="inventory_item_container"]/div/div/div[2]/div[1]'
    INVENTORY_DETAILS_DESC = By.XPATH, '//*[@id="inventory_item_container"]/div/div/div[2]/div[2]'
    INVENTORY_DETAILS_PRICE = By.CLASS_NAME, "inventory_details_price"
