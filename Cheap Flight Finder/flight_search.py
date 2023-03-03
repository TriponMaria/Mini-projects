import os
import requests

TEQUILA_ENDPOINT_LOCATIONS = os.environ['TEQUILA_ENDPOINT_LOCATIONS']
API_KEY = os.environ['API_KEY']

class FlightSearch:
    def get_iata_code(self, city):
        headers = {
            "apikey": API_KEY
        }
        query = {
            "term": city,
            "location_types": "city"
        }
        response = requests.get(TEQUILA_ENDPOINT_LOCATIONS, params=query, headers=headers)
        iata_code = response.json()['locations'][0]["code"]
        return iata_code