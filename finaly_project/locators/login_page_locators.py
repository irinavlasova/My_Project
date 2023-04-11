from selenium.webdriver.common. by import By


class LoginPageLocators:
    LOGO = By.CLASS_NAME, 'Login_logo'
    LOGIN = By.ID, "user-name"
    PASSWORD = By.ID, "password"
    LOGIN_BUTTON = By.ID, "login-button"
    LOGIN_CONTAINER = By.ID, "login_button_container"
    LOGIN_BUTTON_FAIL = By.CLASS_NAME, "error-button"
