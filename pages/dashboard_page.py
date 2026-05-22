class DashboardPage:

    def __init__(self, page):

        self.page = page


    def click_profile_icon(self):

        self.page.locator(
            ".oxd-userdropdown-tab"
        ).click()


    def click_logout(self):

        self.page.locator(
            "text=Logout"
        ).click()