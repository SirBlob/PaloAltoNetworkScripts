### Script to grab the Egress IP Address from your Palo Instance
### Parameters can be changed to your preference
### For More Information - https://docs.paloaltonetworks.com/prisma/prisma-access/3-2/prisma-access-panorama-admin/prisma-access-overview/retrieve-ip-addresses-for-prisma-access

import requests
import json
import re

API_URL = "https://api.prod.datapath.prismaaccess.com/getPrismaAccessIP/v2"
API_KEY = "ADD YOUR API KEY"
HEADERS = {"header-api-key": API_KEY}
PARAMETERS = {"serviceType": "all", "addrType": "all", "location": "all"}

IP_REGEX = r"\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b(?!\/)"
#IP_SUBNET_REGEX = r"\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b(?:\/\d{1,2})?"

def fetch_and_compare_ips():
    """Fetches IPs from the API, compares them to a current list, and reports missing IPs."""

    try:
        response = requests.post(API_URL, headers=HEADERS, data=json.dumps(PARAMETERS).encode())
        response.raise_for_status()
        json_data = response.json()

        ips_from_api = set(re.findall(IP_REGEX, str(json_data)))
        current_ips = set(CURRENT_LIST)

        missing_ips = ips_from_api - current_ips

        if missing_ips:
            print(f"The following IPs are missing from the current list: {missing_ips}")
            print(f"Please ask the vendors to whitelist these IPs and add them to the current list in rundeck.")
        else:
            print("All IPs are in the current list.")

    except requests.exceptions.RequestException as err:
        print("Request failed:", err)
        print("Response status code:", response.status_code)

CURRENT_LIST = [
    # ... (your current IP list here)
]

if __name__ == "__main__":
    fetch_and_compare_ips()
