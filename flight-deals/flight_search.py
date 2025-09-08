import time
from datetime import timedelta

import requests
import os
from dotenv import load_dotenv

load_dotenv()

class FlightSearch:
    def __init__(self):
        self.amadeus_endpoint = os.getenv("AMADEUS_ENDPOINT")
        self.amadeus_key = os.environ.get("AMADEUS_API_KEY")
        self.amadeus_secret = os.environ.get("AMADEUS_API_SECRET")
        self.origin_location = os.environ.get("ORIGIN_LOCATION")

    def get_auth_token(self):
        url = f"{self.amadeus_endpoint}/v1/security/oauth2/token"
        parameters = {
            "grant_type": "client_credentials",
            "client_id": self.amadeus_key,
            "client_secret": self.amadeus_secret
        }
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
        }
        response = requests.post(url, data=parameters, headers=headers).json()
        return response["access_token"]

    def get_iata_code(self, auth_token, city_name):
        endpoint = f'{self.amadeus_endpoint}/v1/reference-data/locations/cities'
        amadeus_city_params = {
            'keyword': city_name.capitalize(),
            'max': 1
        }
        amadeus_headers = {
            "accept": "application/vnd.amadeus+json",
            'Authorization': f"Bearer {auth_token}"
        }
        try:
            iata_code = requests.get(endpoint, params=amadeus_city_params, headers=amadeus_headers).json()
            return iata_code['data'][0]['iataCode']
        except requests.exceptions.RequestException as e:
            return "Not Found"

    def get_flight_details(self, auth_token, iata_code, date, return_date, max_price):
        for_three_months = 5
        endpoint = f'{self.amadeus_endpoint}/v2/shopping/flight-offers'
        amadeus_headers = {
            "accept": "application/vnd.amadeus+json",
            'Authorization': f"Bearer {auth_token}"
        }
        all_flights = []
        for date_offset in range(for_three_months):
            time.sleep(3)
            date = date + timedelta(days=date_offset)
            return_date = return_date + timedelta(days=date_offset)
            amadeus_flight_offers_params = {
                'originLocationCode': self.origin_location,
                'destinationLocationCode': iata_code,
                'departureDate': str(date.strftime("%Y-%m-%d")),
                'returnDate': str(return_date.strftime("%Y-%m-%d")),
                'adults': 1,
                'nonStop': 'false',
                'currencyCode': 'USD',
                'maxPrice': max_price
                # 'max': 5
            }
            try:
                flight_details = requests.get(
                    endpoint,
                    params=amadeus_flight_offers_params,
                    headers=amadeus_headers
                )
                flight_details.raise_for_status()  # will raise if status != 200
                flights = flight_details.json().get('data', [])
                if flights:
                    all_flights.extend(flights)
            except requests.RequestException as e:
                print(f"Error fetching flights for {date}: {e}")
                continue  # skip this date, but keep looping

        return all_flights if all_flights else None