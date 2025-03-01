import os
import subprocess
import sys


def crear_entorno_virtual(nombre_env="venv", requerimientos=None):
    """
    Crea un entorno virtual y asegura que las librerías necesarias estén instaladas.
    Args:
        nombre_env (str): Nombre o ruta del entorno virtual.
        requerimientos (list): Lista de librerías a instalar.
    """
    # Verifica si ya existe la carpeta del entorno virtual
    if not os.path.exists(nombre_env):
        print(f"Creando el entorno virtual en '{nombre_env}'...")
        subprocess.check_call([sys.executable, "-m", "venv", nombre_env])
    else:
        print(f"El entorno virtual '{nombre_env}' ya existe.")

    # Activar el entorno virtual (esto es automático para instalar)
    pip_executable = (
        os.path.join(nombre_env, "Scripts", "pip")
        if os.name == "nt"
        else os.path.join(nombre_env, "bin", "pip")
    )

    # Actualizar pip
    print("Actualizando pip...")
    subprocess.check_call([pip_executable, "install", "--upgrade", "pip"])
    # Instalar los requerimientos si se proporcionan
    if requerimientos:
        print("Instalando las librerías requeridas...")
        subprocess.check_call([pip_executable, "install"] + requerimientos)


if __name__ == "__main__":
    # Nombre del entorno virtual
    nombre_env = "venv"

    # Librerías que quieres instalar
    librerias = ["landingai", "requests", "pandas", "openpyxl", "streamlit", "numpy"]

    # Crear el entorno virtual e instalar las librerías
    crear_entorno_virtual(nombre_env, librerias)
