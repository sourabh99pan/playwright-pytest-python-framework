import pytest
import time
import os
import datetime
from playwright.sync_api import sync_playwright

employee_name = "Sourabh" + str(int(time.time()))


@pytest.fixture
def launch_application(playwright, browser_name):
    """Launch browser using pytest-playwright fixtures and return a `page`.

    Relies on the `playwright` and `browser_name` fixtures provided by
    `pytest-playwright` to parametrize browsers (chromium, firefox, webkit).
    """

    browser = getattr(playwright, browser_name).launch(headless=True)
    context = browser.new_context(viewport={"width": 1920, "height": 1080})
    page = context.new_page()

    page.goto(
        "https://opensource-demo.orangehrmlive.com/",
        wait_until="domcontentloaded",
        timeout=60000,
    )

    yield page

    try:
        context.close()
    except Exception:
        pass
    try:
        browser.close()
    except Exception:
        pass


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        # try to obtain page from common fixture names
        page = item.funcargs.get("page") or item.funcargs.get("launch_application")

        if page:
            os.makedirs("screenshots", exist_ok=True)

            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

            screenshot_name = f"screenshots/{item.name}_{timestamp}.png"

            try:
                page.screenshot(path=screenshot_name, full_page=True)
                print(f"\nScreenshot saved: {screenshot_name}")
            except Exception:
                print("\nFailed to capture screenshot")


def pytest_html_report_title(report):

    report.title = (
        "OrangeHRM Automation Report"
    )