# Unused currently

import config
import requests

api_call = "page/slug/"
slug = "scp-4205"

headers = {"Authorization": "Bearer " + config.scuttle_token}

r = requests.get(
    config.scuttle_endpoint + api_call + slug,
    headers=headers)

print(headers)
print(r)