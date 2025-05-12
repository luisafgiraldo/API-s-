# import asyncio
# from agentic_doc.conversion import convert_file
# from agentic_doc.types import ConversionRequest
# from pathlib import Path
# import requests
# import threading
# from http.server import BaseHTTPRequestHandler, HTTPServer

# --- Simular Webhook Server para recibir notificación ---
# class WebhookHandler(BaseHTTPRequestHandler):
#     def do_POST(self):
#         print("✅ Webhook recibido: Conversión finalizada.")
#         self.send_response(200)
#         self.end_headers()

# def start_webhook_server():
#     server = HTTPServer(('localhost', 8081), WebhookHandler)
#     print("🚀 Webhook escuchando en http://localhost:8081")
#     server.serve_forever()

# --- Simulación de conversión asíncrona ---
# async def async_conversion(file_path: str, webhook_url: str):
#     print(f"⚙️ Iniciando conversión de {file_path}...")
#     await asyncio.sleep(2)  # Simula tiempo de procesamiento
#     output = convert_file(ConversionRequest(file_path=file_path))
#     print(f"📄 Conversión terminada: {output}")
#     requests.post(webhook_url, json={"status": "done", "file": file_path})

# --- Prueba de archivos ---
# def run_tests():
#     🔴 Caso 1: Archivo remoto (fallará)
#     try:
#         print("\n🔴 Intentando conversión remota...")
#         convert_file(ConversionRequest(
#             file_path="https://www.unicef.org/innocenti/reports/accessible-digital-textbooks-nicaragua"  # URL remota falsa
#         ))
#     except Exception as e:
#         print(f"❌ Error esperado en archivo remoto: {e}")

#     🟢 Caso 2: Archivo local exitoso
#     local_file = Path("/Users/luisaaristizabal/Downloads/IndividualesCertificado_77463223_20250424-102448-764.pdf")
#     if not local_file.exists():
#         local_file.write_text("PDF simulado para prueba")  # crear uno dummy

#     print("\n🟢 Conversión local exitosa:")
#     result = convert_file(ConversionRequest(file_path=str(local_file)))
#     print(result)

#     🟠 Caso 3: Conversión asincrónica con webhook simulado
#     print("\n🟠 Iniciando conversión asincrónica...")
#     webhook_thread = threading.Thread(target=start_webhook_server, daemon=True)
#     webhook_thread.start()

#     asyncio.run(async_conversion(str(local_file), "http://localhost:8081"))

# if __name__ == "__main__":
#     run_tests()

# import os
# from agentic_doc.parse import parse_documents

# # Establece tu API Key
# os.environ["VISION_AGENT_API_KEY"] = "aWlqMmo2a2ZpbHA2ODhzY3o5ZGFlOnIzSFI5UnhCV1B5SzRyTHYySTBJSHY4WDZyTHJDaDM0"

# # URL de prueba pública (puedes reemplazar esta por otra PDF pública si quieres)
# test_url = "https://unec.edu.az/application/uploads/2014/12/pdf-sample.pdf"


# # Prueba de procesamiento de un documento remoto
# try:
#     results = parse_documents([test_url])
#     parsed_doc = results[0]

#     print("✅ URL procesada correctamente.")
#     print("Markdown extractado (primeros 500 caracteres):")
#     print(parsed_doc.markdown[:500])
# except Exception as e:
#     print("❌ Error al procesar la URL:")
#     print(e)

from dotenv import load_dotenv
import os

# Load environment variables from the .env file
# Load environment variables from the .env file
load_dotenv()

# Set variables explicitly (opcional pero recomendado para claridad)
# Asignar las variables a las variables de entorno del sistema
endpoint_host = os.getenv("ENDPOINT_HOST")
vision_agent_api_key = os.getenv("VISION_AGENT_API_KEY")

# Verifica que las variables se cargaron correctamente
print(f"Endpoint Host: {endpoint_host}")
print(f"API Key loaded: {vision_agent_api_key}")

from agentic_doc.parse import parse_documents

# Public test URL
test_url = "https://unec.edu.az/application/uploads/2014/12/pdf-sample.pdf"

# Test processing of a remote document
try:
    results = parse_documents([test_url])
    parsed_doc = results[0]

    print("✅ URL processed successfully.")
    print("Extracted Markdown (first 500 characters):")
    print(parsed_doc.markdown[:500])

    # Print the extracted chunks
    print("\n📦 Extracted chunks:")
    for chunk in parsed_doc.chunks:
        print(f"🔹 Chunk ID: {chunk.id}")
        print(f"📝 Text (first 300 characters): {chunk.text[:300]}")
        print(f"⚠️ Chunk type: {chunk.type}\n")

except Exception as e:
    print("❌ Error processing the URL:")
    print(e)
