import requests
from dotenv import load_dotenv
import os
from datetime import datetime

load_dotenv()

user_information = input("Tell me what exercise you did: ")

nutrition_endpoint = os.getenv("NUTRITION_ENDPOINT")
APP_ID = os.getenv('APP_ID')
API_KEY = os.getenv('API_KEY')

nutri_headers = {
    'x-app-id': APP_ID,
    'x-app-key': API_KEY
}

nutri_params = {
    "query": user_information,
    "gender": os.getenv('GENDER'),
    "age": os.getenv('AGE')
}
response = requests.post(nutrition_endpoint, headers=nutri_headers, json=nutri_params)

date = datetime.now().strftime("%d/%m/%Y")
time = datetime.now().strftime("%X")
sheety_endpoint = os.getenv('SHEETY_ENDPOINT')
shetty_headers = {
    "Authorization": os.getenv("AUTH")
}
for exercise in response.json()['exercises']:
    sheety_params = {
        "workout":{
            "date": date,
            "time": time,
            "exercise": exercise['name'].title(),
            "duration": exercise['duration_min'],
            "calories": exercise['nf_calories']
        }
    }
    sheety_response = requests.post(sheety_endpoint,headers=shetty_headers , json=sheety_params)

response = requests.get(sheety_endpoint)