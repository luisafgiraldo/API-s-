# import requests
# import time
# import pytest
# from datetime import datetime

# URL = "https://api.va.staging.landing.ai/v1/tools/agentic-object-detection"
# HEADERS = {
#     "Authorization": "Basic YjgzcW51OHZ0c2w4cnk3bDlsczN4OmlCbFk5RHB4cnNCRndJeW45Y2NsY2hic0VQODBYVzh4",
# }
# DATA = {
#     "prompts": "people",
#     "model": "agentic"
# }
# IMAGE_PATH = r"/Users/luisaaristizabal/Desktop/image1.png"

# def send_request():
#     """Envía solicitudes a la API hasta recibir un 429 o un código de error."""
#     request_count = 0  # Contador de solicitudes
#     start_time = time.time()  # Tiempo de inicio global
    
#     while True:
#         request_count += 1
#         request_start_time = time.time()
        
#         with open(IMAGE_PATH, "rb") as image_file:
#             files = {"image": image_file}
#             response = requests.post(URL, files=files, data=DATA, headers=HEADERS)
        
#         request_end_time = time.time()
#         request_duration = request_end_time - request_start_time  # Duración de la solicitud

#         timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#         print(f"[{timestamp}] Request #{request_count}: Status {response.status_code}, Duration: {request_duration:.2f}s")

#         if response.status_code == 429:
#             total_duration_seconds = request_end_time - start_time
#             hours, remainder = divmod(total_duration_seconds, 3600)
#             minutes, seconds = divmod(remainder, 60)

#             print(f"Request #{request_count} received a 429 Too Many Requests error. Stopping.")
#             print(f"Time elapsed since script start until error: {int(hours)} hours, {int(minutes)} minutes, {seconds:.2f} seconds.")
#             return request_count, response.status_code
        
#         # if not (200 <= response.status_code < 300):
#         #     print(f"Request #{request_count} encountered an error: {response.status_code}")
#         #     return request_count, response.status_code

# @pytest.mark.parametrize("expected_status", [200, 429])
# def test_api_request(expected_status):
#     """Prueba la API asegurando que los códigos de respuesta sean 200 o 429."""
#     request_count, last_status = send_request()
    
#     assert request_count > 0, "No se realizaron solicitudes, posible error en la configuración."
#     assert last_status in [200, 429], f"Se recibió un código inesperado: {last_status}"

import pytest
import requests
import time
import logging

# Configurar logging para pytest
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

URL = "https://api.va.staging.landing.ai/v1/tools/agentic-object-detection"
HEADERS = {
    "Authorization": "Basic eTdiN3pjM2dpbWlhbnIwMzJlcDdvOnFoTlZZNDIwTk9ORDV4U3M5UVA3R0JZN1VrS3JhVXV0",
}
DATA = {
    "prompts": "people",
    "model": "agentic"
}
IMAGE_PATH = r"/Users/luisaaristizabal/Desktop/image1.png"


def test_api_requests():
    request_count = 0  # Contador de solicitudes
    start_time = time.time()  # Tiempo de inicio global

    while True:
        request_count += 1
        request_start_time = time.time()

        with open(IMAGE_PATH, "rb") as image_file:
            files = {"image": image_file}
            response = requests.post(URL, files=files, data=DATA, headers=HEADERS)

        request_end_time = time.time()
        request_duration = request_end_time - request_start_time

        logger.info(
            f"Request #{request_count}: Status {response.status_code}, Duration: {request_duration:.2f} sec"
        )

        # Verificar que la respuesta no sea None
        assert response is not None, "La respuesta de la API es None."
        # Verificar que el código de respuesta sea válido
        assert response.status_code != 500, "Error 500 - Internal Server Error"
        assert response.status_code != 403, "Error 403 - Forbidden. Verifica las credenciales."
        
        if response.status_code == 429:
            total_duration_seconds = request_end_time - start_time
            hours, remainder = divmod(total_duration_seconds, 3600)
            minutes, seconds = divmod(remainder, 60)

            logger.warning(
                f"Request #{request_count} recibió un 429 Too Many Requests. Deteniendo."
            )
            logger.warning(
                f"Tiempo transcurrido: {int(hours)}h {int(minutes)}m {seconds:.2f}s"
            )
            break
        
        assert 200 <= response.status_code < 300, f"Error: Código de estado {response.status_code}"
