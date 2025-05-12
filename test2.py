import requests
import time

url = "https://api.va.staging.landing.ai/v1/tools/agentic-document-analysis"
headers = {
    "Authorization": "Basic aWlqMmo2a2ZpbHA2ODhzY3o5ZGFlOnIzSFI5UnhCV1B5SzRyTHYySTBJSHY4WDZyTHJDaDM0"
}


start_time = time.time()

with open("/Users/luisaaristizabal/Downloads/Marco_Aurelio_Meditaciones_50_pages (1).pdf", "rb") as f:
    files = {"pdf": f}
    response = requests.post(url, files=files, headers=headers)


end_time = time.time()
elapsed_time = end_time - start_time

print("Status Code:", response.status_code)
print("Response Text:", response.text)
print(f"Tiempo de ejecución: {elapsed_time:.2f} segundos")
output_path = "/Users/luisaaristizabal/Downloads/response_output.txt"
with open(output_path, "w", encoding="utf-8") as out_file:
    out_file.write(response.text)

print(f"✅ Response guardado en {output_path}")


# import requests

# url = "https://api.va.staging.landing.ai/v1/tools/agentic-object-detection"

# files = {
#   "image": open("/Users/luisaaristizabal/Downloads/car.jpg", "rb")
# }

# data = {
#   "prompts": "car",
#   "model": "agentic"
# }

# headers = {
#   "Authorization": "Basic aWlqMmo2a2ZpbHA2ODhzY3o5ZGFlOnIzSFI5UnhCV1B5SzRyTHYySTBJSHY4WDZyTHJDaDM0"
# }

# response = requests.post(url, files=files, data=data, headers=headers)

# print(response.json())


