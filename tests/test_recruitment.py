import pytest

from pages.login_page import LoginPage
from pages.recruitment_page import RecruitmentPage
from utils.logger import setup_logger

logger = setup_logger()

class TestRecruitmentModule:

    @pytest.mark.smoke
    def test_001_recruitment_search_by_job_title(self, launch_application):
        page = launch_application
        login = LoginPage(page)
        recruitment = RecruitmentPage(page)

        login.enter_username("Admin")
        logger.info("Enter username")
        login.enter_password("admin123")
        logger.info("Enter password")
        login.click_login()
        logger.info("Click on login button")

        recruitment.click_recruitment()
        recruitment.wait_for_recruitment_page()
        recruitment.select_job_title("Automaton Tester")
        recruitment.click_search()

        page.wait_for_timeout(3000)
        assert "recruitment" in page.url.lower()
        assert recruitment.has_search_results() or recruitment.get_no_records_text() == "No Records Found"

    @pytest.mark.regression
    def test_recruitment_search_by_vacancy(self, launch_application):
        page = launch_application
        login = LoginPage(page)
        recruitment = RecruitmentPage(page)

        login.enter_username("Admin")
        logger.info("Enter username")
        login.enter_password("admin123")
        logger.info("Enter password")
        login.click_login()
        logger.info("Click on login button")

        recruitment.click_recruitment()
        recruitment.wait_for_recruitment_page()
        recruitment.select_vacancy("Payroll Administrator")
        recruitment.click_search()

        page.wait_for_timeout(3000)
        assert "recruitment" in page.url.lower()
        assert recruitment.has_search_results() or recruitment.get_no_records_text() == "No Records Found"

    @pytest.mark.regression
    def test_003_recruitment_search_by_job_title_and_vacancy(self, launch_application):
        page = launch_application
        login = LoginPage(page)
        recruitment = RecruitmentPage(page)

        login.enter_username("Admin")
        logger.info("Enter username")
        login.enter_password("admin123")
        logger.info("Enter password")
        login.click_login()
        logger.info("Click on login button")

        recruitment.click_recruitment()
        recruitment.wait_for_recruitment_page()
        recruitment.select_job_title("Automaton Tester")
        recruitment.select_vacancy("Payroll Administrator")
        recruitment.click_search()

        page.wait_for_timeout(3000)
        assert "recruitment" in page.url.lower()
        assert recruitment.has_search_results() or recruitment.get_no_records_text() == "No Records Found"