import requests
import datetime
from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()

ALPHA_API_KEY = os.getenv('ALPHA_API_KEY')
NEWS_API_KEY = os.getenv('NEWS_API_KEY')
start_date = datetime.date.today()
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": ALPHA_API_KEY
}

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = f"https://newsapi.org/v2/everything"


def fetch_news_stock():
    news_parameters = {
        'qInTitle': STOCK,
        'from': str(start_date),
        'sortBy': 'relevancy',
        'language': 'en',
        'apiKey': NEWS_API_KEY
    }
    news = requests.get(NEWS_ENDPOINT, params=news_parameters).json()
    titles = []
    descriptions = []
    for item in news['articles']:
        titles.append(item['title'])
        descriptions.append(item['description'])

    return titles[:3], descriptions[:3]

def send_message(coded, titles, descriptions):
    account_sid = os.getenv('account_sid')
    auth_token = os.getenv('auth_token')
    client = Client(account_sid, auth_token)
    messages = [f"Heading: {x}\nBrief: {y}" for x, y in zip(titles, descriptions)]
    for message in messages:
        whatsapp_message = client.messages.create(
            from_=f'whatsapp:{os.getenv('FROM')}',
            body=f"{STOCK}: {coded} \n{message}",
            to=f'whatsapp:{os.getenv('TO')}'
        )
        print(whatsapp_message.sid)

def get_stock_price():
    data_list = [value for (key,value) in stock_data.items()]
    yesterday_data = data_list[0]['4. close']
    day_before_data = data_list[1]['4. close']
    print(yesterday_data, day_before_data)
    return yesterday_data, day_before_data


stock_response = requests.get(STOCK_ENDPOINT, params=stock_parameters).json()

stock_data = stock_response["Time Series (Daily)"]
yesterday_price, day_before_price = get_stock_price()

difference = abs(float(yesterday_price) - float(day_before_price))*100/float(day_before_price)

if difference > 1 and float(yesterday_price) > float(day_before_price):
    coded_message = f"🔺{int(difference)}"
    title, description = fetch_news_stock()
    send_message(coded_message, title, description)
elif float(yesterday_price) < float(day_before_price):
    print("No News")
    coded_message = f"🔻{int(difference)}"
    title, description = fetch_news_stock()
    send_message(coded_message, title, description)

