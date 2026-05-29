from pages.login_page import LoginPage
from pages.recruitment_page import RecruitmentPage
from utils.logger import setup_logger

logger = setup_logger()

def test_search_candidate(launch_application):

    page = launch_application

    login = LoginPage(page)

    login.enter_username("Admin")

    logger.info("Enter username")

    login.enter_password("admin123")

    logger.info("Enter password")

    login.click_login()

    logger.info("Click on login button")

    recruitment = RecruitmentPage(page)

    recruitment.click_recruitment()

    recruitment.select_job_title("Automaton Tester")

    recruitment.select_vacancy("Payroll Administrator")

    recruitment.click_search()