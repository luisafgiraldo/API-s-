import env
import utils as u
from utils import browser

TOOL_NAME = "Agentic Object Detection"


def test_agentic_object_detection(browser):
    """Ejecuta la prueba para todos los elementos de env.ELEMENTS_OD en un ciclo for."""

    # Iniciar sesión
    page = u.login(browser)

    # Navegar a la API
    u.navigate_to_explore_apis(page)
    u.navigate_tool(page, TOOL_NAME)

    # Iterar sobre cada elemento de prueba
    for element in env.ELEMENTS_OD:
        print(f"🔍 Probando con el elemento: {element}")

        # Esperar que la página cargue completamente antes de cada interacción
        page.wait_for_load_state("networkidle")

        # Intentar hacer clic en la imagen
        try:
            img_selector = f"img[alt*='{element}']"
            page.wait_for_selector(img_selector, timeout=20000)
            u.click_image(page, element)
        except Exception as e:
            print(f"⚠️ No se encontró la imagen '{element}': {e}")
            continue  # Salta al siguiente elemento en la lista

        print("⏳ Esperando 50 segundos...")
        u.time_step(50)

        # Definir la ruta de la imagen capturada
        captured_image_path = env.CAPTURED_IMAGE_PATH.format(element.replace(" ", "_"))

        # Capturar pantalla del elemento SVG
        svg_element = page.locator("svg.relative.size-full")
        svg_element.screenshot(path=captured_image_path)
        print(f"📸 Captura de pantalla guardada: {captured_image_path}")

        # Obtener la imagen de referencia correcta
        reference_image_path = env.REFERENCES_OD.get(element)
        if reference_image_path:
            if u.compare_images(captured_image_path, reference_image_path):
                print("✅ Las imágenes coinciden")
                # Opción para eliminar la imagen capturada
                u.remove_image(captured_image_path)
            else:
                print("❌ Las imágenes son diferentes")
        else:
            print(f"⚠️ No se encontró imagen de referencia para: {element}")

        # 🔄 Recargar el navegador después de procesar cada imagen
        print("🔄 Recargando la página para el siguiente elemento...")
        page.reload()
