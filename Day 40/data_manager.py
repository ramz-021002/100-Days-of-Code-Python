import os
import requests
from dotenv import load_dotenv


# Load environment variables from .env file
load_dotenv()

SHEETY_PRICES_ENDPOINT = os.getenv('SHEETY_PRICES_ENDPOINT')

class DataManager:

    def __init__(self):
        self.auth = os.getenv("SHEETY_AUTH")
        self.sheety_headers = {
            "Authorization": self.auth
        }
        self.destination_data = {}

    def get_destination_data(self):
        # Use the Sheety API to GET all the data in that sheet and print it out.
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, headers=self.sheety_headers)
        data = response.json()
        self.destination_data = data["prices"]
        # Try importing pretty print and printing the data out again using pprint() to see it formatted.
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data,
                headers = self.sheety_headers
            )
            # print(response.text)
