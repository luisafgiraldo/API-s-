from agentic_doc.parse import parse_documents
from dotenv import load_dotenv
import os
import time  # Importar time para medir duración

def main():
    # Cargar el archivo .env
    load_dotenv()

    # Verificar si el API Key está cargado
    api_key = os.getenv("VISION_AGENT_API_KEY")
    if not api_key:
        raise ValueError("No se encontró VISION_AGENT_API_KEY en el entorno. Verifica tu archivo .env.")

    # Lista de documentos locales
    file_paths = [
        "/Users/luisaaristizabal/Downloads/Marco_Aurelio_Meditaciones_100_pages.pdf"
    ]

    # Iniciar contador de tiempo
    start_time = time.time()

    # Procesar los documentos
    results = parse_documents(file_paths)

    # Finalizar contador de tiempo
    end_time = time.time()
    elapsed_time = end_time - start_time

    # Mostrar los resultados
    for idx, parsed_doc in enumerate(results):
        print(f"\n--- Resultado para {file_paths[idx]} ---\n")
        print("Markdown extraído:")
        print(parsed_doc.markdown)
        print("\nChunks estructurados:")
        for chunk in parsed_doc.chunks:
            print(chunk)

    # Mostrar el tiempo que tardó
    print(f"\nTiempo total de procesamiento: {elapsed_time:.2f} segundos")

if __name__ == "__main__":
    main()

