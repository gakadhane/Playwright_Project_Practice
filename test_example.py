import re
from playwright.sync_api import Page, expect
from playwright.sync_api import sync_playwright
from pytest_playwright.pytest_playwright import browser

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless = False, slow_mo=500)
    page = browser.new_page()

def test_has_title(page: Page):
    page.goto("https://playwright.dev/")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Playwright"))

def test_get_started_link(page: Page):
    page.goto("https://playwright.dev/")

    # Click the get started link.
    page.get_by_role("link", name="Get started").click()

    # Expects page to have a heading with the name of Installation.
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()