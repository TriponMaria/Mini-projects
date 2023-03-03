#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import requests
from data_manager import DataManager
from flight_data import FlightData
from flight_search import FlightSearch
from notification_manager import NotificationManager

data = DataManager()
sheet_data = data.get_data()


for city in sheet_data:
    if not city["iataCode"]:
        city["iataCode"] = FlightSearch().get_iata_code(city["city"])
    flight = FlightData()
    flight_data = flight.get_data_flight("LON", city["iataCode"], city["lowestPrice"])
    flight.best_deals()
    sms = NotificationManager()
    if flight.price:
        sms.send_sms(flight.price, flight.fly_from, flight.fly_to, flight.date_departure, flight.date_arrival)

data.update_data()







