import requests
import time

# PDF path
pdf_path = "page-limit/pdfs/Marco_Aurelio_Meditaciones_101_pages.pdf""

# Definition of tiers and their expected responses
tiers = [
    {
        "name": "tier1",
        "api_key": "cXc3OHczMmhkMmY3a3QxaHJrc3lhOlVqUzM0U3lrM1BqczlKN0tJMVNxRnJFOExhcmpWbHM1",
        "expected_status": 422,
        "expected_message": "PDF must not exceed 50 pages."
    },
    {
        "name": "tier2",
        "api_key": "eTcyM3p2eHloMTQ2Y25xdmg0YXl6OlV0cnAxdFVNVGk1VUpKcUUzMzNqNFZMSmZRRjYwTnRu",
        "expected_status": 422,
        "expected_message": "PDF must not exceed 50 pages."
    },
    {
        "name": "tier3",
        "api_key": "YW1ocTZseGltNzM1Z2txdmVpNWNzOnVqV0FvVEQ1eHlMSzNqVDA0Mkg0NzJ0RTVQU1ZFQ1JG",
        "expected_status": 422,
        "expected_message": "PDF must not exceed 100 pages."
    }
]

url = "https://api.va.staging.landing.ai/v1/tools/agentic-document-analysis"

for tier in tiers:
    print(f"\n🔍 Testing {tier['name']}")

    headers = {
        "Authorization": f"Basic {tier['api_key']}"
    }

    start_time = time.time()

    with open(pdf_path, "rb") as f:
        files = {"pdf": f}
        response = requests.post(url, files=files, headers=headers)

    end_time = time.time()
    elapsed_time = end_time - start_time

    print("Status Code:", response.status_code)
    print("Response Text:", response.text)
    print(f"⏱ Execution time: {elapsed_time:.2f} seconds")

    # Try-except block to continue execution even if an assertion fails
    try:
        assert response.status_code == tier["expected_status"], f"Unexpected status code: {response.status_code}"
        assert tier["expected_message"] in response.text, f"Unexpected error message: {response.text}"
        print(f"✅ {tier['name']} passed all validations.")
    except AssertionError as e:
        print(f"❌ {tier['name']} failed: {e}")

# Summary
print("\n📋 Test Summary:")
for name, result in results:
    print(f"- {name}: {result}")


# === API Credential References for Tiers ===

# Tier 1:
# Email: luisa.aristizabal.external+Tier1ADE@landing.ai
# Password: Luisa2336097
# API Key (Base64 encoded): cXc3OHczMmhkMmY3a3QxaHJrc3lhOlVqUzM0U3lrM1BqczlKN0tJMVNxRnJFOExhcmpWbHM1

# Tier 2:
# Email: luisa.aristizabal.external+Tier2ADE@landing.ai
# Password: Luisa2336097
# API Key (Base64 encoded): eTcyM3p2eHloMTQ2Y25xdmg0YXl6OlV0cnAxdFVNVGk1VUpKcUUzMzNqNFZMSmZRRjYwTnRu

# Tier 3:
# Email: luisa.aristizabal.external+Tier3ADE@landing.ai
# Password: Luisa2336097
# API Key (Base64 encoded): YW1ocTZseGltNzM1Z2txdmVpNWNzOnVqV0FvVEQ1eHlMSzNqVDA0Mkg0NzJ0RTVQU1ZFQ1JG
