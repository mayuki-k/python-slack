import requests
import json
from env import const

payload = {"text":"There is an error"}
response = requests.post(const.WEB_HOCK_URL, data=json.dumps(payload))
print(response.text)