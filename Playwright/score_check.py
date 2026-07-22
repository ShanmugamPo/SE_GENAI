from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False,args=["--start-maximized"])

    context = browser.new_context(no_viewport=True)
    page = context.new_page()

    page.goto("https://www.cricbuzz.com/")
    page.wait_for_timeout(3000)  # Wait for 3 seconds to ensure the page is fully loaded
    popup_button = page.get_by_role("button", name="Consent", exact=True)

    if popup_button.is_visible():
        popup_button.click()
        page.wait_for_timeout(2000)  # Wait for 2 seconds after clicking the button

    page.click("text=Live Scores")
    screenshot = page.screenshot(path="cricbuzz_homepage.png")
    browser.close()




