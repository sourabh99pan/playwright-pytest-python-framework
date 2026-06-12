import pytest

from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage
from utils.logger import setup_logger

logger = setup_logger()


def login_to_dashboard(page):
    login = LoginPage(page)
    login.enter_username("Admin")
    login.enter_password("admin123")
    login.click_login()

    page.wait_for_url("**/dashboard/**")
    logger.info("Logged in and navigated to Dashboard")

    return DashboardPage(page)


def test_101_dashboard_title_and_url(launch_application):
    page = launch_application
    dashboard = login_to_dashboard(page)

    assert dashboard.is_dashboard_loaded()
    assert "dashboard" in page.url.lower()
    assert dashboard.get_dashboard_title().strip() == "Dashboard"


def test_102_dashboard_widgets_visible(launch_application):
    page = launch_application
    dashboard = login_to_dashboard(page)

    assert dashboard.is_time_at_work_visible()
    assert dashboard.is_my_actions_visible()
    assert dashboard.is_quick_launch_visible()
    assert dashboard.is_buzz_latest_posts_visible()
    assert dashboard.is_employees_on_leave_visible()


def test_103_dashboard_search_box_accepts_input(launch_application):
    page = launch_application
    dashboard = login_to_dashboard(page)

    dashboard.search_in_dashboard("PIM")
    assert page.locator("input[placeholder='Search']").input_value() == "PIM"


def test_104_navigate_to_pim_from_dashboard(launch_application):
    page = launch_application
    dashboard = login_to_dashboard(page)

    dashboard.click_pim_module()
    page.wait_for_url("**/pim/**")
    assert "/pim/" in page.url.lower()


def test_105_dashboard_logout(launch_application):
    page = launch_application
    dashboard = login_to_dashboard(page)

    dashboard.logout()
    page.wait_for_url("**/auth/login**")
    assert "login" in page.url.lower()
