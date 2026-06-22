import pytest
import time
import os
import datetime
import pathlib
import re
import json
from playwright.sync_api import sync_playwright

employee_name = "Sourabh" + str(int(time.time()))

def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        default="qa",
        help="Environment name"
    )

@pytest.fixture(scope="session")
def config(request):
    env = request.config.getoption("--env")
    with open(f"config/{env}.json") as file:
        return json.load(file)


@pytest.fixture
def launch_application(playwright, browser_name, request, config):
    """Launch browser using pytest-playwright fixtures and return a `page`.

    Relies on the `playwright` and `browser_name` fixtures provided by
    `pytest-playwright` to parametrize browsers (chromium, firefox, webkit).
    """

    # Check if the --headed flag was used in the terminal execution command
    is_headed_passed = request.config.getoption("--headed", default=False)
    
    # If --headed is passed, headless mode must be False; otherwise, default to True
    headless = False if is_headed_passed else True

    browser = getattr(playwright, browser_name).launch(headless=headless)
    context = browser.new_context(
        viewport={"width": 1920, "height": 1080},
        record_video_dir="artifacts/videos",
        record_video_size={"width": 1920, "height": 1080},
    )
    page = context.new_page()

    page.goto(
        config["base_url"],
        wait_until="domcontentloaded",
        timeout=config["timeout"],
    )

    video = None
    try:
        yield page
        video = page.video
    except Exception:
        raise
    finally:
        try:
            context.close()
        except Exception:
            pass
        try:
            browser.close()
        except Exception:
            pass
        if video:
            try:
                os.makedirs("artifacts/videos", exist_ok=True)
                safe_name = re.sub(r"[^A-Za-z0-9_.-]", "_", request.node.name)
                filename = f"artifacts/videos/{safe_name}_{browser_name}.webm"
                video.save_as(filename)
                original_path = pathlib.Path(video.path())
                if original_path.exists() and original_path != pathlib.Path(filename):
                    try:
                        original_path.unlink()
                    except Exception:
                        pass
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
    report.title = "OrangeHRM Automation Report"