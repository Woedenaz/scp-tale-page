import config
import requests

headers = {"Authorization": "Bearer " + config.scuttle_token}
r = requests.get(config.scuttle_endpoint + '/v1/page', headers=headers).json()

print(headers)
print(r)