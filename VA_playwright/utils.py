import os
import pytest
import env
import time
from PIL import Image, ImageChops
from playwright.sync_api import sync_playwright
import pyautogui

@pytest.fixture(scope="function")
def browser():
    screen_width, screen_height = pyautogui.size()  # Obtiene el tamaño de la pantalla
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(viewport={"width": screen_width, "height": screen_height})
        yield context
        browser.close()


def compare_images(img1_path, img2_path):
    """Compara dos imágenes y verifica si son similares dentro de un umbral de diferencia."""
    img1 = Image.open(img1_path).convert("RGB")
    img2 = Image.open(img2_path).convert("RGB")
    diff = ImageChops.difference(img1, img2)
    diff_bbox = diff.getbbox()
    return diff_bbox is None  # Si no hay diferencias significativas, devuelve True


def login(browser):
    """ Realiza el inicio de sesión y devuelve la página cargada. """
    page = browser.new_page()
    page.goto(env.URL, timeout=60000)

    # Iniciar sesión
    page.fill("input[name='identifier']", env.USERNAME)
    page.get_by_role("button", name="Sign in").click()
    page.fill("input[name='password']", env.PASSWORD)
    page.get_by_role("button", name="Continue").click()
    print("✅ Login exitoso")
    
    return page  # Retornamos la página para reutilizarla

def navigate_to_explore_apis(page):
    """ Navega a la sección 'Explore APIs' después del login. """
    page.wait_for_selector("div:text('What vision task do you have in mind?')", timeout=10000)
    page.get_by_role("button", name="Explore APIs").click()
    print("✅ Click en 'Explore APIs'")
    

def navigate_tool(page, tool):
    """ Navega hasta la opción 'Agentic Object Detection'. """
    page.wait_for_selector(f"p:text('{tool}')", timeout=10000)
    page.locator(f"p:text('{tool}')").click()
    print(f"✅ Click en '{tool}'")
    page.wait_for_selector(f"div:text('{tool}')", timeout=10000)
    print(f"✅ Validación exitosa: '{tool}' está visible")

def click_image(page, element_name):
    """Hace clic en la imagen del elemento especificado."""
    page.wait_for_selector(f"div.relative.flex.size-full img[alt='{element_name}']", timeout=10000)
    page.locator(f"div.relative.flex.size-full img[alt='{element_name}']").click(force=True)
    print(f"✅ Click en la imagen del {element_name}")

    # Esperar a que aparezca el elemento PromptTips
    page.wait_for_selector("div[data-sentry-component='PromptTips']", timeout=10000)
    print("✅ Elemento PromptTips visible")

    # Click en el botón verde
    page.wait_for_selector("button.bg-green-500")
    page.locator("button.bg-green-500").click()
    print("✅ Click en botón verde")

def time_step(iterator : int):
    return time.sleep(iterator)


def remove_image(image_path):
    """Elimina una imagen si el usuario lo confirma."""
    if os.path.exists(image_path):
        os.remove(image_path)
        print(f"✅ Archivo eliminado: {image_path}")
    else:
        print(f"⚠️ El archivo no existe: {image_path}")

