import requests
import time
import os

url = "https://api.va.staging.landing.ai/v1/tools/agentic-document-analysis"

headers = {
    "Authorization": "Basic YW1ocTZseGltNzM1Z2txdmVpNWNzOnVqV0FvVEQ1eHlMSzNqVDA0Mkg0NzJ0RTVQU1ZFQ1JG",
}

image_paths = [
    "measuring_time/pdf/1966 Corvette.jpeg",
    "measuring_time/pdf/Camaro Sport Coupe .jpeg"
]

summary = []
errors = []
num_requests_per_image = 10

for image_path in image_paths:
    image_name = os.path.basename(image_path)
    
    for i in range(1, num_requests_per_image + 1):
        with open(image_path, "rb") as image_file:
            files = {"image": image_file}

            start_time = time.time()
            response = requests.post(url, files=files, headers=headers)
            duration = time.time() - start_time

            status_code = response.status_code

            if status_code != 200:
                errors.append(f"{image_name} | Run {i} failed with status code {status_code}")

            summary.append({
                "image": image_name,
                "run": i,
                "status": status_code,
                "time": f"{duration:.3f} seconds"
            })

# Summary 
print("\n===== TEST SUMMARY =====")
for result in summary:
    print(f"Image: {result['image']} | Run: {result['run']} | Status: {result['status']} | Time: {result['time']}")
print("=========================")


if errors:
    print("\n❌ Some tests failed:")
    for e in errors:
        print(f"- {e}")
    raise Exception("One or more image requests failed.")
else:
    print("\n✅ All image requests succeeded.")
