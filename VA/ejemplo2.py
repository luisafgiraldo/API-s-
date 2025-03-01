import requests

url = "https://api.dev.landing.ai/v1/tools/document-analysis"
files = {
  "image": open(r"C:\Users\user\Desktop\Image2.png", "rb")
}
data = {
  "parse_text": True,
  "parse_tables": True,
  "parse_figures": True,
  "summary_verbosity": "normal",
  "caption_format": "json",
  "response_format": "json",
  "return_chunk_crops": False,
  "return_page_crops": False
}


response = requests.post(url, files=files, data=data)

print(response.json())
