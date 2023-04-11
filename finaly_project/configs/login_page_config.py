from finaly_project.configs.main_config import MainConfig


class Login_Page_Config(MainConfig):
    def __init__(self):
        super().__init__()
        self.URL_CURRENT = self.URL + "inventory.html"
        self.USER_NAME = "standard_user"
        self.LOCKED_OUT_USER = "locked_out_user"
        self.PROBLEM_USER = "problem_user"
        self.PERFORMANCE_GLITCH_USER = "performance_glitch_user"
        self.PASSWORD_USER = "secret_sauce"
        self.error_text = "Epic sadface: Username is required"
