import pytest

from pages.login_page import LoginPage
from utils.json_reader import read_json
from utils.logger import setup_logger


data = read_json("testdata/login_data.json")
logger = setup_logger()

@pytest.mark.parametrize(
    "test_data",
    data["login_data"]
)

@pytest.mark.smoke
def test_001_login_data_driven(
        launch_application,
        test_data
):

    page = launch_application

    logger.info("In test_001_login_data_driven")

    logger.info("Starting login data driven test")

    login = LoginPage(page)

    login.enter_username(
        test_data["username"]
    )

    logger.info("Username entered")

    login.enter_password(
        test_data["password"]
    )

    logger.info("Password entered")

    login.click_login()

    page.wait_for_timeout(3000)

    if test_data["expected"] == "Pass":

        page.wait_for_url("**/dashboard/**")

        assert "dashboard" in page.url.lower()

        logger.info("dashboard in URL verified successfully")

    else:

        error_message = login.get_error_message()

        assert "Invalid credentials" in error_message

        logger.info("Invalid credentials displayed")


def test_002_page_title(launch_application):

    logger.info("In test_002_page_title")

    page = launch_application

    logger.info("Starting page title test")

    assert "OrangeHRM" in page.title()

    logger.info("Page title verified successfully")


def test_003_failed_login_screenshot(launch_application):

    page = launch_application
    
    logger.info("In test_003_failed_login_screenshot")

    logger.info("Starting page title test")


    login = LoginPage(page)

    login.enter_username("Admin")

    login.enter_password("admin123")

    login.click_login()

    page.wait_for_url("**/dashboard/**")

    logger.info("dashboard in URL verified successfully")

    page.wait_for_selector("h6")

    assert "Google" in page.title()