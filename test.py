import requests

url = "https://api.va.staging.landing.ai/v1/tools/text-to-instance-segmentation"

video_path = "/Users/luisaaristizabal/Downloads/Test scenarios for the explore tools section/Florence-2 Sam2 Image/stock-photo-apples-collection-isolated-on-white-background-2489589621.jpg"

files = {
  "image": open(video_path, "rb")
}


data = {
  "prompt": "apple",
  "model": "florence2sam2"
}

headers = {
  "Authorization": "Basic eTdiN3pjM2dpbWlhbnIwMzJlcDdvOnFoTlZZNDIwTk9ORDV4U3M5UVA3R0JZN1VrS3JhVXV0"
}

response = requests.post(url, files=files, data=data, headers=headers)

print("Status code:", response.status_code)
print("Response text:", response.text)
