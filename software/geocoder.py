import requests

API_KEY = "YOUR_OPENCAGE_KEY"


def get_location(lat, lon):
    url = f"https://api.opencagedata.com/geocode/v1/json?q={lat}+{lon}&key={API_KEY}"

    response = requests.get(url).json()

    if response['results']:
        return response['results'][0]['formatted']

    return "Location not found"
