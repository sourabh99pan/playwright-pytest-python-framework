from playwright.sync_api import Page

class RecruitmentPage:

    def __init__(self, page: Page):
        self.page = page

    def click_recruitment(self):
        self.page.get_by_role("link", name="Recruitment").click()

    def select_job_title(self, job_title):
        self.page.locator("(//div[contains(@class,'oxd-select-text')])[1]").click()
        self.page.get_by_text(job_title).click()

    def select_vacancy(self, vacancy_name):

        self.page.locator("//label[text()='Vacancy']/../following-sibling::div").click()

        self.page.get_by_role(
            "option",
            name=vacancy_name
        ).click()

    def click_search(self):
        self.page.get_by_role("button", name="Search").click()