import requests
import os
from dotenv import load_dotenv

load_dotenv()


class DataManager:
    def __init__(self):
        self.auth = os.getenv("SHEETY_AUTH")
        self.endpoint = os.getenv("SHEETY_ENDPOINT")
        self.sheety_headers = {
            "Authorization": self.auth
        }

    def get_data(self):
        data = requests.get(self.endpoint, headers=self.sheety_headers).json()
        return data['prices']

    def add_iada_code(self, filed_id, iata_code):
        data = {
            'price': {
                "iataCode": iata_code
            }
        }
        response = requests.put(f'{self.endpoint}/{filed_id}', headers=self.sheety_headers, json=data)


