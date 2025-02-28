import requests
url = "https://api.staging.landing.ai/v1/tools/agentic-object-detection"
headers = {
    "Authorization": "Basic eTdiN3pjM2dpbWlhbnIwMzJlcDdvOnFoTlZZNDIwTk9ORDV4U3M5UVA3R0JZN1VrS3JhVXV0"
}
image_path = r"C:\Users\user\Desktop\image.jpg"
# Petición malformada sin el parámetro "model"
data = {
    "prompts": ["dogs"]
}
with open(image_path, "rb") as file:
    files = {"image": file}
    response = requests.post(url, files=files, data=data, headers=headers)
print(f"Status Code: {response.status_code}")
print("Response:", response.text)