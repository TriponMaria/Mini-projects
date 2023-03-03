import os
import requests

SHEET_ENDPOINT = os.environ['SHEET_ENDPOINT']


class DataManager:
    def __init__(self):
        self.sheet_data = {}

    def get_data(self):
        sheet_response = requests.get(url=SHEET_ENDPOINT)
        self.sheet_data = sheet_response.json()["prices"]
        return self.sheet_data

    def update_data(self):
        for city in self.sheet_data:
            parameters = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            requests.put(f"{SHEET_ENDPOINT}//{city['id']}", json=parameters)




