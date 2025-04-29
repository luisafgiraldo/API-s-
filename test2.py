import requests

url = "https://api.va.staging.landing.ai/v1/tools/agentic-document-analysis"
files = {
    "image": open("/Users/luisaaristizabal/Downloads/fam_tree1.jpg", "rb")
}
headers = {
    "Authorization": "Basic eTdiN3pjM2dpbWlhbnIwMzJlcDdvOnFoTlZZNDIwTk9ORDV4U3M5UVA3R0JZN1VrS3JhVXV0"
}

response = requests.post(url, files=files, headers=headers)

print("Status Code:", response.status_code)
print("Response Text:", response.text)
# import requests

# url = "https://api.va.landing.ai/v1/tools/agentic-object-detection"

# files = {
#   "image": open("/Users/luisaaristizabal/Downloads/car.jpg", "rb")
# }

# data = {
#   "prompts": "car",
#   "model": "agentic"
# }

# headers = {
#   "Authorization": "Basic OHZkbzZ1aWUxMjExMXIwaGg3NzE1OkxZZ0hURUttc2lUWTRXNlRPdjBnNlFtMjNoUmhMTEVI"
# }

# response = requests.post(url, files=files, data=data, headers=headers)

# print(response.json())


