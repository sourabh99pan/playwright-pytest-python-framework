import pytest
import time


employee_name = "Sourabh" + str(int(time.time()))


@pytest.fixture
def launch_application(page):

    page.set_viewport_size({"width": 1920, "height": 1080})

    page.goto(
        "https://opensource-demo.orangehrmlive.com/",
        wait_until="domcontentloaded",
        timeout=60000
    )

    return page

@pytest.hookimpl(hookwrapper=True)

def pytest_runtest_makereport(item, call):

    outcome = yield

    report = outcome.get_result()

    if report.when == "call" and report.failed:

        page = item.funcargs.get("page")

        if page:

            page.wait_for_timeout(3000)

            screenshot_name = f"screenshots/{item.name}.png"

            page.screenshot(
                path=screenshot_name,
                full_page=True
            )

            print(f"Screenshot saved: {screenshot_name}")

def pytest_html_report_title(report):

    report.title = "OrangeHRM Automation Report"