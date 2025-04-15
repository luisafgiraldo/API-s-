import os
import requests
import pytest
from dotenv import load_dotenv

load_dotenv()

BASE_PATH = "/Users/luisaaristizabal/Documents/cereal"

@pytest.fixture(scope="session")
def api_headers():
    return {
        "apikey": "land_sk_aohoNQYFNkQAARrEUennlu27nC1eafY8ui36CHge2sRMeANLJz",
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

@pytest.fixture(scope="session")
def created_project(api_headers):
    url = "https://api.staging.landing.ai/v1/projects"
    payload = {
        "name": "test_anomaly_upload14april",
        "projectType": "anomaly-detection"
    }
    response = requests.post(url, json=payload, headers=api_headers)
    assert response.status_code in [200, 201], f"Error creating project: {response.status_code} - {response.text}"

    return response.json()["data"]["id"]

def test_upload_images_and_train(api_headers, created_project):
    folders = ["clean", "contaminated"]
    folder_to_label = {
        "clean": "normal",
        "contaminated": "abnormal",
    }

    for folder in folders:
        folder_path = os.path.join(BASE_PATH, folder)
        assert os.path.exists(folder_path), f"Missing folder: {folder_path}"
        images = os.listdir(folder_path)
        assert len(images) > 0, f"No images found in {folder_path}"

        for image_file in images:
            image_path = os.path.join(folder_path, image_file)
            with open(image_path, "rb") as image_data:
                files = {
                    "file": (
                        image_file,
                        image_data,
                        "image/jpeg"
                    )
                }
                payload = {
                    "name": image_file,
                    "label": folder_to_label[folder],
                    "tags": ["test", "automation"],
                }

                url = f"https://api.staging.landing.ai/v1/projects/{created_project}/images"
                res = requests.post(
                    url,
                    headers={"apikey": api_headers["apikey"]},
                    files=files,
                    data=payload
                )
                assert res.status_code == 200, f"Upload failed for {image_file}: {res.status_code} - {res.text}"

    # Paso 1: Auto Split con constraints para anomaly
    autosplit_url = f"https://api.staging.landing.ai/v1/projects/{created_project}/autosplit"
    autosplit_payload = {
        "splitPercentages": {
            "train": 65,
            "dev": 25,
            "test": 10,
        },
        "selectOption": "all-labeled",
        "constraints": {
            "train": {
                "labels": ["normal"]
            },
            "dev": {
                "labels": ["normal", "abnormal"]
            },
            "test": {
                "labels": ["normal", "abnormal"]
            }
        }
    }

    autosplit_response = requests.post(autosplit_url, headers={"apikey": api_headers["apikey"]}, json=autosplit_payload)
    assert autosplit_response.status_code == 201, f"Auto split failed: {autosplit_response.status_code} - {autosplit_response.text}"
    print("✅ Auto split done!")

    # Paso 2: Entrenamiento
    training_url = "https://app.staging.landing.ai/api/model/train"
    payload = {
        "projectId": created_project,
        "experimentType": "anomaly-detection"
    }

    response = requests.post(training_url, headers=api_headers, json=payload)

    assert response.status_code == 200, f"Training failed: {response.status_code} - {response.text}"
    print("✅ Training started successfully!")



