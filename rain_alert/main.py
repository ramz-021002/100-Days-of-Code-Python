import requests
from twilio.rest import Client
api_key = "<OPEN WEATHER API KEY>"
LAT = "<LATITUDE>"
LON = "<LONGITUDE>"
OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"

account_sid = '<TWILIO ACCOUNT SID>'
auth_token = '<TWILIO AUTH TOKEN>'
client = Client(account_sid, auth_token)

parameters = {
    'lat': LAT,
    'lon': LON,
    'appid': api_key,
    'cnt': 4
}

response = requests.get(OWM_ENDPOINT, params=parameters)
response.raise_for_status()

weather_data = response.json()
# print(weather_data)

weather_ids = []
for data in weather_data['list']:
    weather_ids.append(data['weather'][0]['id'])

# print(weather_ids)

if any(x < 700 for x in weather_ids):
    message = client.messages.create(
        from_="whatsapp:TWILIO_WHATSAPP_NUMBER",
        body="It's going to rain today. Remember to bring an umbrella",
        to="whatsapp:YOUR_TWILIO_VERIFIED_NUMBER"
    )
    print(message.sid)
else:
    print("No Rain Today")


