import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 37.2431
MY_LOG = 115.7930
EMAIL_ADDRESS = '<EMAIL>'
PASSWORD = '<PASSWORD>'

def compare_locations():
    response = requests.get(url='http://api.open-notify.org/iss-now.json')
    response.raise_for_status()
    
    data = response.json()
    
    latitude = float(data['iss_position']['latitude'])
    longitude = float(data['iss_position']['longitude'])
    print(latitude, longitude)
    if (MY_LAT - 5 <= latitude <= MY_LAT + 5) and (MY_LOG - 5 <= latitude <= MY_LOG + 5):
        return True
    else:
        return False

def is_dark():
    time_now = datetime.now()
    current_hour = time_now.hour
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LOG,
        "formatted": 0,
        "tzid": "America/New_York"
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    if current_hour >= sunset or current_hour <= sunrise:
        return True
    else:
        return False

def send_email(message):
    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()

        connection.login(EMAIL_ADDRESS, PASSWORD)
        connection.sendmail(
            from_addr=EMAIL_ADDRESS,
            to_addrs="<EMAIL>",
            msg=f"Subject: 'Look for ISS'\n\n {message}"
        )



while True:
    if compare_locations() & is_dark():
        send_email("Look up on the sky for ISS")
    else:
        print("Look Down")
    time.sleep(60)