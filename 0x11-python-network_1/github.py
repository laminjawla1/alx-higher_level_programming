import requests
import json


username = "laminjawla1"
url = f"https://api.github.com/users/{username}"

response = requests.get(url)
out = json.loads(response.text)

print(out)