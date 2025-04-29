import requests
import concurrent.futures
import time

def send_request(results):
    url = "https://api.va.staging.landing.ai/v1/tools/florence2"
    files = {"image": open("/Users/luisaaristizabal/Downloads/fam_tree1.jpg", "rb")}
    data = {"prompts": "detect aircraft"}
    headers = {"Authorization": "Basic eTdiN3pjM2dpbWlhbnIwMzJlcDdvOnFoTlZZNDIwTk9ORDV4U3M5UVA3R0JZN1VrS3JhVXV0"}
    
    while True:
        response = requests.post(url, files=files, data=data, headers=headers)
        results.append(response.status_code)
        
        if response.status_code == 429:
            print("Received 429 Too Many Requests")
            break
        elif response.status_code == 200:
            print("Received 200 OK, retrying...")
            time.sleep(1)  # Espera antes de reintentar
        else:
            print(f"Received {response.status_code}: {response.text}")
            break

results = []
with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
    futures = [executor.submit(send_request, results) for _ in range(50)]
    concurrent.futures.wait(futures)

print(f"Total 429 responses: {results.count(429)}")
print(f"Total 200 responses: {results.count(200)}")
