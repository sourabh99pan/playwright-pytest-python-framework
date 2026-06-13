from pages.base_page import BasePage


class RecruitmentPage(BasePage):

    def __init__(self, page):
        super().__init__(page)

    RECRUITMENT_MENU = "a:has-text('Recruitment')"
    JOB_TITLE_SELECT = "(//div[contains(@class,'oxd-select-text')])[1]"
    VACANCY_SELECT = "//label[text()='Vacancy']/../following-sibling::div"
    SEARCH_BUTTON = "button:has-text('Search')"
    SEARCH_RESULTS = "div.oxd-table-body div[role='row']"
    NO_RECORDS_FOUND = "span:has-text('No Records Found')"
    OPTION_ROW = "div[role='option']"

    def click_recruitment(self):
        self.click(self.RECRUITMENT_MENU)

    def wait_for_recruitment_page(self):
        self.page.locator(self.JOB_TITLE_SELECT).wait_for()

    def select_job_title(self, job_title):
        self.click(self.JOB_TITLE_SELECT)
        option = self.page.locator(f"{self.OPTION_ROW}:has-text('{job_title}')")
        option.wait_for(timeout=10000)
        option.click()

    def select_vacancy(self, vacancy_name):
        self.click(self.VACANCY_SELECT)
        option = self.page.locator(f"{self.OPTION_ROW}:has-text('{vacancy_name}')")
        option.wait_for(timeout=10000)
        option.click()

    def click_search(self):
        self.click(self.SEARCH_BUTTON)

    def wait_for_search_results(self):
        self.page.locator(self.SEARCH_RESULTS).first.wait_for(timeout=10000)

    def has_search_results(self):
        return self.page.locator(self.SEARCH_RESULTS).count() > 0

    def get_no_records_text(self):
        return self.page.locator(self.NO_RECORDS_FOUND).text_content()
