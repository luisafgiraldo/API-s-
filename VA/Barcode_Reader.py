import requests
import pandas as pd
import utils as u


def create(url: str, image_path: str):
    querystring = {"timeout": "300"}

    # Crear el payload
    payload = {"image": u.transformer(image_path)}

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
    }

    try:
        # Enviar solicitud POST
        response = requests.post(url, json=payload, headers=headers, params=querystring)

        # Comprobación del response_data
        if response.status_code == 200:
            response_data = response.json()
            print(response_data)
            print(
                "\033[32m"
                + "============================== 1 passed Barcode_Reader.py =============================="
                + "\x1b[0m"
            )
        else:
            print(f"Error {response.status_code}: {response.text}")
            print(
                f"\033[31m"
                + "============================== 1 failed Barcode_Reader.py =============================="
                + "\x1b[0m"
            )
            return pd.DataFrame()  # DataFrame vacío en caso de error
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
        print(
            f"\033[31m"
            + "============================== 1 failed Barcode_Reader.py =============================="
            + "\x1b[0m"
        )
        return pd.DataFrame()  # DataFrame vacío en caso de error
