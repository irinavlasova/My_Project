from selenium. webdriver.common. by import By


class BasePageLocators:
    LOGO = By. CLASS_NAME, 'app_logo'
    TITLE = By.CLASS_NAME, "title"
    SHOPPING_CART = By.ID, "shopping_cart_container"

    SIDE_MENU = By. CLASS_NAME, 'bm-burger-button'
    BUTTON_CLOSE_MENU = By.ID, "react-burger-cross-btn"
    INVENTORY_SIDEBAR = By.ID, "inventory_sidebar_link"
    ABOUT_SIDEBAR = By.ID, "about_sidebar_link"
    LOGOUT_SIDEBAR = By.ID, "logout_sidebar_link"
    RESET_SIDEBAR = By.ID, "reset_sidebar_link"
    SHOPPING_CART_MENU = By.ID, "react-burger-menu-btn"

    TWITTER = By.LINK_TEXT, "Twitter"
    FACEBOOK = By.CLASS_NAME, "social_facebook"
    LINKEDIN = By.CLASS_NAME, "social_linkedin"
    FOOTER_COPY = By.CLASS_NAME, "footer_copy"
