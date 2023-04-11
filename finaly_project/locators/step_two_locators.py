from selenium.webdriver.common. by import By


class TwoPageLocators:
    CANCEL = By.ID, "cancel"
    FINISH = By.ID, "finish"

    QTY = By.CLASS_NAME, "cart_quantity_label"
    DESCRIPTION = By.CLASS_NAME, "cart_desc_label"

    PAYMENT_INF = By.XPATH, '//*[@id="checkout_summary_container"]/div/div[2]/div[1]'
    SAUCECARD = By.XPATH, '//*[@id="checkout_summary_container"]/div/div[2]/div[2]'
    SHOPPING_INF = By.XPATH, '//*[@id="checkout_summary_container"]/div/div[2]/div[3]'
    DELIVERY = By.XPATH, '//*[@id="checkout_summary_container"]/div/div[2]/div[4]'
    PRICE_TOTAL = By.XPATH, '//*[@id="checkout_summary_container"]/div/div[2]/div[5]'

    ITEM_TOTAL = By.XPATH, '//*[@id="checkout_summary_container"]/div/div[2]/div[6]'
    TAX = By.XPATH, '//*[@id="checkout_summary_container"]/div/div[2]/div[7]'
    TOTAL = By.XPATH, '//*[@id="checkout_summary_container"]/div/div[2]/div[8]'
