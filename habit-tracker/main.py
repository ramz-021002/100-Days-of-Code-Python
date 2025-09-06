from datetime import date
import os
from http.client import responses

from dotenv import load_dotenv
import requests
load_dotenv()
pixela_endpoint = 'https://pixe.la/v1/users'

user_parameters = {
    'token': os.getenv('PIXEL_TOKEN'),
    'username': os.getenv('PIXEL_USERNAME'),
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}

# response = requests.post(url=pixela_endpoint, json=user_parameters)
# print(response.json())

graph_endpoint = f'{pixela_endpoint}/{os.getenv('PIXEL_USERNAME')}/graphs'
graph_headers = {
    'X-USER-TOKEN': os.getenv('PIXEL_TOKEN'),
}
graph_body = {
    "id": os.getenv('PIXEL_GRAPH_ID'),
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "momiji"
}

# response = requests.post(graph_endpoint, json=graph_body, headers=graph_headers)
# print(response.json())

plex_endpoint = f'{graph_endpoint}/{os.getenv('PIXEL_GRAPH_ID')}'

pixel_body = {
    'date': date.today().strftime("%Y%m%d"),
    'quantity': '6.969'
}

response = requests.post(plex_endpoint, json=pixel_body, headers=graph_headers)
print(response.json())
