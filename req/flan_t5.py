# To test Requests
import requests

url_dev = "http://localhost:8000"

body = {"prompt": "Tell me a joke"}
response = requests.post(f"{url_dev}/flan-t5", json=body)
print(response.json())