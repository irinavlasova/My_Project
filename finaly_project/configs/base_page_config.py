from finaly_project.configs.main_config import MainConfig


class BasePageConfig(MainConfig):
    def __init__(self):
        super().__init__()
        self.URL_CURRENT_BASE = self.URL + "inventory.html"
        self.URL_CURRENT_BASE_MENU = "https://saucelabs.com/"
        self.URL_SHOPPING_CART_PAGE = self.URL + "cart.html"
        self.text_logo = "Swag Labs"
        self.title_logo = "Products"
        self.URL_TWITTER = "https://twitter.com/saucelabs"
        self.URL_facebook = "https://www.facebook.com/saucelabs"
        self.URL_linkedin = 'https://www.linkedin.com/company/sauce-labs/?original_referer='
        self.URL_linkedin_two = "https://www.linkedin.com/authwall?trk=bf&trkInfo=AQEHvZclkMUHUwAAAYcPoc34SixlrSOxEOQ" \
                                "5HSasqOQgNxUXVGRWv_caE_JsR5l4XzA4X0ZRwbIXvh7SiOjqori5e6FkXCUeFKhFE-xfwUu9kGZryTuENhP" \
                                "X0j_k90tHGSY4ffo=&original_referer=&sessionRedirect=https%3A%2F%2Fwww.linkedin.com%" \
                                "2Fcompany%2Fsauce-labs%2F"
        self.text_copy = "© 2023 Sauce Labs. All Rights Reserved. Terms of Service | Privacy Policy"
