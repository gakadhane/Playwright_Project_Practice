

import condition
from playwright.sync_api import sync_playwright, Playwright
import pytest

@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as playwright:
        yield playwright

@pytest.mark.regression
def test_darebee_website(playwright_instance):
    # Launch browser
    browser = playwright_instance.chromium.launch(headless=False, slow_mo=500)

    # Open new page
    page = browser.new_page()

    # Navigate to a web page
    page.goto("https://darebee.com/")

    # Print page title and run assertions
    print(page.title())
    assert "DAREBEE - Home Workouts" in page.title()
    assert page.text_content("title") == "DAREBEE - Home Workouts"

    # Perform actions - click and input
    page.locator("//div[@class='topmenu']//ul[1]//li[1]//a[@href='/workouts.html']").click()
    page.click("//div[@class='category-desc clearfix']//a[@href='/filter']")
    page.fill("//input[@class='input-text']", "UPPER")

    # Take screenshot
    page.screenshot(path="darebee_screenshot.png")
    print("Test completed: workout")

    browser.close()

@pytest.mark.sanity
def test_google_search(playwright_instance):
    # Launch browser
    browser = playwright_instance.chromium.launch(headless=False, slow_mo=3000)
    context = browser.new_context()

    # Start tracing before creating / navigating a page.
    context.tracing.start(screenshots=True, snapshots=True, sources=True)

    page = context.new_page()
    page.goto("https://www.google.com/")
    page.locator("#gws-output-pages-elements-homepage_additional_languages__als").click()
    page.get_by_role("img", name="Google").click()
    page.get_by_role("button", name="Google Search").click()
    page.get_by_role("button", name="Google Search").click()
    page.get_by_role("combobox", name="शोधा").click()
    page.get_by_role("combobox", name="शोधा").fill("playwright")
    page.get_by_role("button", name="व्हॉइसद्वारे शोधा").click()
    page.get_by_role("button", name = "test")

    # Stop tracing and export it into a zip archive.
    context.tracing.stop(path="google_trace.zip")
    print("Test completed: Google search")

    context.close()
    browser.close()


@pytest.mark.skip(reason="Skipping this test for now")
@pytest.mark.sanity
def test_example():
    assert 1 == 1


@pytest.mark.skipif(condition, reason="Skip if condition is True")
@pytest.mark.regression
def test_example():
    assert 1 == 1


@pytest.mark.xfail(reason="Known issue")
@pytest.mark.sanity
def test_example():
    assert 1 == 2


@pytest.mark.xfail(condition, reason="Expected to fail if condition is True")
@pytest.mark.regression
def test_example():
    assert 1 == 2