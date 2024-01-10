import requests
import json

api_key = "YOUR-API-KEY"
api_url = "https://api.prod.datapath.prismaaccess.com/getPrismaAccessIP/v2"
headers = {"header-api-key": api_key}
parameters = {"serviceType": "all", "addrType": "all", "location": "all"}
param_bytes = json.dumps(parameters).encode() #for some odd reason it has to be in bytes format

try:
    response = requests.post(api_url, headers=headers, data=param_bytes)
    response.raise_for_status()

    print("Response status code:", response.status_code)
    print("Response data:")
    print(response.json())

except requests.exceptions.RequestException as err:
    print("Request failed:", err)
    if response:
        print("Error response:")
        print(response.json())