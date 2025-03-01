# Credenciales
USERNAME = "luisa_aristizabal23211@elpoli.edu.co"
PASSWORD = "dots&lines&tests1496"
URL = "https://va.staging.landing.ai/"

# Lista de elementos a probar
ELEMENTS_OD = [
    "batsman",
    "black coffee in a cup with saucer",
    "windows with room lights on",
    "pipe wrench",
    "occupied table",
    "frame with city map",
]

# Diccionario con rutas de imágenes de referencia
import os

IMAGES_PATH_BASE = os.path.join("VA_playwright", "Images")
REFERENCES_OD = {
    "batsman": os.path.join(IMAGES_PATH_BASE, "Batsman.png"),
    "black coffee in a cup with saucer": os.path.join(
        IMAGES_PATH_BASE, "image_black_coffee_in_a_cup_with_saucer.png"
    ),
    "windows with room lights on": os.path.join(
        IMAGES_PATH_BASE, "image_windows_with_room_lights_on.png"
    ),
    "pipe wrench": os.path.join(IMAGES_PATH_BASE, "image_pipe_wrench.png"),
    "occupied table": os.path.join(IMAGES_PATH_BASE, "image_occupied_table.png"),
    "frame with city map": os.path.join(
        IMAGES_PATH_BASE, "image_frame_with_city_map.png"
    ),
}


# Formato de la imagen capturada (usando placeholders)
CAPTURED_IMAGE_PATH = os.path.join(
    "VA_playwright", "CaptureImages", "captured_image_{}.png"
)
