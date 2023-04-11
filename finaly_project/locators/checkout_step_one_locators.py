from selenium.webdriver.common.by import By


class CheckoutPageLocators:
    FIRST_NAME = By.ID, "first-name"
    LAST_NAME = By.ID, "last-name"
    POSTAL_CODE = By.ID, "postal-code"
    CANCEL = By.ID, "cancel"
    CONTINUE = By.ID, "continue"
    ERROR = By.TAG_NAME, "h3"
