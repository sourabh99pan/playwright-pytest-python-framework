import pytest
import time
from pages.login_page import LoginPage
from pages.pim_page import PimPage
from conftest import employee_name
from pages.dashboard_page import DashboardPage
from utils.logger import setup_logger

logger = setup_logger()

@pytest.mark.regression
def test_004_employee_workflow(launch_application):

    page = launch_application

    logger.info("In test_004_employee_workflow")

    logger.info("Starting page title test")

    employee_id = str(int(time.time()))[-5:]

    login = LoginPage(page)

    # Login

    login.enter_username("Admin")

    logger.info("Enter username")

    login.enter_password("admin123")

    logger.info("Enter password")

    login.click_login()

    logger.info("Click on login button")

    page.wait_for_url("**/dashboard/**")

    pim = PimPage(page)

    # Open PIM Module

    pim.click_pim_menu()

    logger.info("Click on pim menu")

    # Add Employee

    pim.click_add_employee()

    logger.info("Click on add employee")

    pim.wait_for_add_employee_page()

    pim.enter_first_name(employee_name)

    logger.info("Enter employee first name")

    pim.enter_last_name("Pandya")

    logger.info("Enter employee last name")

    pim.enter_employee_id(employee_id)

    logger.info("Enter employee id")

    pim.click_submit_button()

    logger.info("Click on submit button")

    page.wait_for_url("**/viewPersonalDetails/**")

    page.wait_for_timeout(3000)

    assert "viewPersonalDetails" in page.url

    logger.info("Validate viewPersonalDetails in url")

    # Search Employee

    page.wait_for_load_state("networkidle")

    page.wait_for_timeout(3000)

    pim.click_pim_menu()

    logger.info("Click on pim menu")

    pim.search_employee_name(employee_name)

    logger.info("Search employee")

    pim.click_submit_button()

    logger.info("Click on submit button")

    page.wait_for_timeout(3000)

    assert pim.verify_employee_name(employee_name)

    logger.info("Verify employee")

    # Delete Employee

    pim.select_employee_checkbox()

    pim.click_delete_button()

    pim.confirm_delete()

    logger.info("Delete employee")

    page.wait_for_timeout(3000)

    dashboard = DashboardPage(page)

    dashboard.click_profile_icon()

    dashboard.click_logout()

    logger.info("Logout from application")

    page.wait_for_url("**/auth/login")

    assert "login" in page.url.lower()

    logger.info("Validate login page after logout")

    page.wait_for_timeout(5000)