import time

from data_manager import DataManager
from flight_data import find_cheapest_price
from flight_search import FlightSearch
import requests
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta

dataManager = DataManager()
flight = FlightSearch()
auth_token = flight.get_auth_token()

sheet_data = dataManager.get_data()


for i in range(len(sheet_data)):

    if sheet_data[i]['iataCode'] == '':
        city_name = sheet_data[i]['city']
        filed_id = sheet_data[i]['id']
        iada_code = flight.get_iata_code(auth_token, city_name)
        print(iada_code)
        dataManager.add_iada_code(filed_id, iada_code)
        sheet_data = dataManager.get_data()
    else:
        pass

    max_price = sheet_data[i]['lowestPrice']
    date = datetime(2025, 10,2,00,00,00) + timedelta(days=1)
    return_date = date + timedelta(days=60)
    print(f"Finding cheapest price for {sheet_data[i]['iataCode']}")
    flights = flight.get_flight_details(
        auth_token,
        sheet_data[i]['iataCode'],
        date,
        return_date,
        max_price
    )
    time.sleep(5)
    cheapest_flight = find_cheapest_price(flights)
    print(f"{sheet_data[i]['iataCode']}: ${cheapest_flight.price}")



