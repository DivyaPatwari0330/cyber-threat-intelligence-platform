import requests

API_KEY = "4e937b35653c8b9c5c5f9901e534a69982d4ae71860aebf039d3454319526c64c33b375e592fa110"

def check_ip(ip):

    url = "https://api.abuseipdb.com/api/v2/check"

    headers = {
        "Key": API_KEY,
        "Accept": "application/json"
    }

    params = {
        "ipAddress": ip,
        "maxAgeInDays": "90"
    }

    response = requests.get(
        url,
        headers=headers,
        params=params
    )

    return response.json()
