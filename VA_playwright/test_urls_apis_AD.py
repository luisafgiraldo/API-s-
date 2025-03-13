import pytest
import env
import utils as u
from utils import browser

BASE_API_URL = "https://api.va.staging.landing.ai/v1/tools/"

# List of the tools
TOOLS = {
    "Agentic Object Detection": "agentic-object-detection",
    "Agentic Document Extraction": "agentic-document-analysis",
}

@pytest.fixture(scope="module")
def logged_in_page(browser):
    """Login once and return the page instance."""
    page = u.login(browser)
    return page

def test_validate_all_tools(browser):
    """Iterates over all tools, validates 'View API' presence, verifies the URL, and returns to the tools list."""

    # Step 1: Login to the platform
    page = u.login(browser)
    # 🕒 wait 10 seconds after login
    print("🕒 Waiting 10 seconds after login...")
    page.wait_for_timeout(10000)

    # Step 2: Navigate directly to the demo page (sin Explore APIs ni View all APIs)
    demo_url = "https://va.staging.landing.ai/demo"
    print(f"🌐 Navigating to {demo_url}")
    page.goto(demo_url, wait_until="load")

    # Step 3: Esperar a que la lista de herramientas cargue
    page.wait_for_selector("div.overflow-hidden.text-ellipsis.text-lg.font-semibold.text-gray-50", timeout=10000)

    for tool_name, endpoint in TOOLS.items():
        print(f"🔄 Validating tool: {tool_name}")

        # Step 5: Select and click on the tool
        tool_button = page.locator(f"div.overflow-hidden.text-ellipsis.text-lg.font-semibold.text-gray-50:has-text('{tool_name}')")
        assert tool_button.is_visible(), f"❌ '{tool_name}' button not found"
        
        tool_button.click()
        print(f"✅ Clicked on '{tool_name}'")

        # Step 6: 🕒 Wait for 5 seconds to allow all elements to load
        page.wait_for_timeout(5000)  

        # Step 7: Detect which "View API" button to use
        if tool_name == "Agentic Object Detection":
            view_api_button = page.locator("button[data-sentry-element='Button'][class*='bg-primary']")
        elif tool_name == "Agentic Document Extraction":
            view_api_buttons = page.locator("button:has-text('View API')")
            print("🔍 Botones encontrados:", view_api_buttons.count())
        else:
            raise ValueError(f"❌ No selector defined for tool: {tool_name}")

        
        assert view_api_button.is_visible(), f"❌ 'View API' button not found for {tool_name}"

        # Hace clic en el botón
        view_api_button.click(force=True)
        print("✅ Clicked on 'View API'")

        # Step 8: Wait for the API details dialog to appear
        page.wait_for_selector("div[role='dialog']", timeout=10000)

        # Step 9: Validate the API URL inside the tool
        expected_url = f"{BASE_API_URL}{endpoint}"
        api_url_element = page.locator(f"span.token:text('{expected_url}')")

        actual_url = api_url_element.text_content().strip('"') if api_url_element.is_visible() else None

        print(f"🔍 Expected Base URL: {expected_url}")
        print(f"🔍 Found URL on Page: {actual_url}")

        # Step 10: Fail the test if the URL does not match
        assert actual_url == expected_url, f"❌ URL mismatch! Expected: {expected_url}, but found: {actual_url}"
        print(f"✅ URL validated successfully for {tool_name}: {expected_url}")

        # Step 11: Return to the tools list using browser back function
        page.go_back()
        print("✅ Returned to the tools list using browser back")

        # Step 12: Wait for the tools list to load again before continuing
        page.wait_for_selector("div.overflow-hidden.text-ellipsis.text-lg.font-semibold.text-gray-50", timeout=10000)

    # Step 13: Close the browser after testing all tools
    browser.close()
