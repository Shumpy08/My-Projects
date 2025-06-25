# This file will need to use the DataManager,FlightSearch,
# FlightData, NotificationManager classes to achieve the program requirements.

import requests

from data_manager import DataManager
from flight_search import FlightSearch

sheety_api = "https://api.sheety.co/5578977c2f83834148ce4c60bd1fa87d/flightDeals/prices"
response = requests.get(url=sheety_api)
# pprint(response.json()["prices"])
data = response.json()
sheet_data = DataManager().get_destination_data()
print(sheet_data)
TEQUILA_API = "4Qj5-hr59cyUN2RJWGF3bL6NjoJEY8HN"
TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
if sheet_data[0]["iataCode"] == "":
    flight_search = FlightSearch(sheet_data)
    flight_search.get_destination()
    print(sheet_data)
    # for row in sheet_data:
    #     row["iataCode"] = flight_search.get_destination_code(row["city"])
    # print(f"sheet_data:\n {sheet_data}")
    #
    # data_manager.destination_data = sheet_data
    # data_manager.update_destination_codes()
