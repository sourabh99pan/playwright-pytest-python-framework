from pages.base_page import BasePage


class LoginPage(BasePage):

    def __init__(self, page):

        self.page = page


    def enter_username(self, username):

        self.fill(
            "[name='username']",
            username
        )


    def enter_password(self, password):

        self.page.locator("[name='password']").fill(password)


    def click_login(self):

        self.click(
            "button[type='submit']"
        )

    def get_error_message(self):

        return self.page.locator(".oxd-alert-content-text").text_content()