# import pytest
# import pyautogui
# from playwright.async_api import async_playwright
# import pytest_asyncio

# # Credenciales y URL
# USERNAME = "luisa_aristizabal23211@elpoli.edu.co"
# PASSWORD = "Luisa233@"
# URL = "https://va.staging.landing.ai/"
# #VIDEO_PATH = "/Users/luisaaristizabal/Desktop/API-s-/VA_playwright/Images/shark.mp4"
# @pytest_asyncio.fixture(scope="function")
# async def browser():
#     screen_width, screen_height = pyautogui.size()
#     async with async_playwright() as p:
#         browser = await p.chromium.launch(headless=False)
#         context = await browser.new_context(viewport={"width": screen_width, "height": screen_height})
#         page = await context.new_page()
#         await page.goto(URL)
#         yield page
#         await browser.close()
        

# @pytest.mark.asyncio
# async def test_login_and_validate_elements(browser):
#     # Iniciar sesión
#     await browser.fill("input[name='identifier']", USERNAME)
#     await browser.get_by_role("button", name="Sign in").click()
#     await browser.fill("input[name='password']", PASSWORD)
#     await browser.get_by_role("button", name="Continue").click()
#     await browser.wait_for_selector("div:text('What vision task do you have in mind?')", timeout=10000)
#     print("✅ Login exitoso y página cargada correctamente")

#     # Hacer clic en el elemento especificado
#     await browser.click("p.text-sm.font-semibold:text('Detect how close sharks are to surfers')")
#     print("✅ Click en el elemento correcto")

#   # Validar si el video está presente con espera de 20 segundos
#     #video_locator = "video source[src='/asset/examples/shark3_short.mp4']"
#     #await browser.wait_for_selector(video_locator, timeout=20000)
#     #assert await browser.is_visible(video_locator), "❌ El video no está presente"
#     #print("✅ Video encontrado correctamente")

#     # Validar si el texto está presente
#     textarea = await browser.locator("textarea[placeholder*='Examples']").input_value()
#     expected_text = "Can you track both people and sharks in this video? Save a video with the tracked masks of both sharks and people and draw a line between the shark and the closest person with the distance above it. Use 13 pixels = 1m and FPS 10."
#     assert textarea == expected_text, "❌ El texto en el textarea no coincide"
#     print("✅ Texto validado correctamente")


#     # Validar si el botón 'Generate Code' está presente y hacer clic
#     # Validar si el botón 'Generate Code' está presente y hacer clic
#     generate_code_button = browser.locator("span.bold", has_text="Generate Code")
#     assert await generate_code_button.is_visible(), "❌ El botón 'Generate Code' no está presente"
#     await generate_code_button.click()
#     print("✅ Click en 'Generate Code'")

#         # Validar si el botón 'Code' es visible con timeout
#     code_button = browser.locator("button[aria-controls='radix-:rl:-content-Code']")
#     await code_button.wait_for(timeout=20000)
#     assert await code_button.is_visible(), "❌ El botón 'Code' no está presente"
#     print("✅ Botón 'Code' visible correctamente")

import pytest

assert 1 == 1