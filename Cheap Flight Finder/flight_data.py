import datetime as dt
import os
import requests

TEQUILA_ENDPOINT_SEARCH = os.environ['TEQUILA_ENDPOINT_SEARCH']
API_KEY = os.environ['API_KEY']
DATE_FROM = dt.date.today()
DATE_TO = DATE_FROM + dt.timedelta(6*365/12)

class FlightData:
    def __init__(self):
        self.data = []
        self.fly_from = ""
        self.fly_to = ""
        self.price = 0
        self.date_departure = ''
        self.date_arrival = ''

    def get_data_flight(self, fly_from, fly_to, price_to):
        headers = {
            "apikey": API_KEY
        }

        parameters = {
            "fly_from": fly_from,
            "fly_to": fly_to,
            "date_from": str(DATE_FROM.strftime("%d/%m/%Y")),
            "date_to": str(DATE_TO.strftime("%d/%m/%Y")),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "price_to": str(price_to),
            "max_stopovers": 0
        }

        response = requests.get(TEQUILA_ENDPOINT_SEARCH, params=parameters, headers=headers)
        self.data = response.json()["data"]
        if self.data:
            self.data = self.data[0]
        return self.data

    def best_deals(self):
        if self.data:
            self.price = self.data["price"]
            self.fly_from = f"{self.data['route'][0]['cityFrom']}-{self.data['route'][0]['flyFrom']}"
            self.fly_to = f"{self.data['route'][0]['cityTo']}-{self.data['route'][0]['flyTo']}"
            self.date_departure = self.data["route"][0]["local_departure"][:10]
            self.date_arrival = self.data["route"][1]["local_arrival"][:10]


