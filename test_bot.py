import requests
from requests.auth import HTTPBasicAuth
import json

headers = {'TRN-Api-key': '69d87d1e-38f2-4537-87f7-a2e5d9625901'}

response = requests.get("https://public-api.tracker.gg/v2/csgo/standard/profile/steam/goatinahat",headers=headers)
#print(response.status_code)
#print(response.json())
print(json.dumps(response.json(), indent=1))


data = json.loads(response.text)

#["userInfo"]["segments"]["stats"]

i = 0

stats = data["data"]

for key, item in stats.items():
    print(item["platformUserId"])