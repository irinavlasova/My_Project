from selenium.webdriver.common.by import By


class FinishPageLocators:
    BACK_HOME = By.ID, "back-to-products"
    COMPLETE = By.CLASS_NAME, "pony_express"
    COMPLETE_MESSAGE = By.CLASS_NAME, "complete-header"
    COMPLETE_TEXT = By.CLASS_NAME, "complete-text"
