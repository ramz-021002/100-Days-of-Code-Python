import requests
import datetime
from twilio.rest import Client

ALPHA_API_KEY = "<>"
NEWS_API_KEY = "<>"
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
        'q': STOCK,
        'from': str(start_date),
        'sortBy': 'relevancy',
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
    account_sid = '<>'
    auth_token = '<>'
    client = Client(account_sid, auth_token)
    messages = [f"Heading: {x}\nBrief: {y}" for x, y in zip(titles, descriptions)]
    for message in messages:
        whatsapp_message = client.messages.create(
            from_="whatsapp:TWILIO_WHATSAPP_NUMBER",
            body=f"{STOCK}: {coded} \n{message}",
            to="whatsapp:YOUR_TWILIO_VERIFIED_NUMBER"
        )
        print(whatsapp_message.sid)
def get_stock_price(yesterday, day_before):
    global start_date
    yesterday_data = 0
    day_before_data = 0
    if str(yesterday) not in stock_data:
        yesterday -= datetime.timedelta(days=1)
        day_before -= datetime.timedelta(days=1)
        if str(day_before) not in stock_data:
            day_before -= datetime.timedelta(days=1)

    if (stock_data[str(yesterday)] is not None) and str(day_before) in stock_data :
        yesterday_data = stock_data[str(yesterday)]['4. close']
        day_before_data = stock_data[str(day_before)]['4. close']
        start_date = yesterday
        return yesterday_data, day_before_data
    else:
        return get_stock_price(yesterday, day_before-datetime.timedelta(days=1))


stock_response = requests.get(STOCK_ENDPOINT, params=stock_parameters).json()
stock_response.raise_for_status()
stock_data = stock_response["Time Series (Daily)"]

yesterday_date = datetime.date.today() - datetime.timedelta(days=1)
day_before_yesterday = yesterday_date - datetime.timedelta(days=1)
yesterday_price, day_before_price = get_stock_price(yesterday_date, day_before_yesterday)

difference = abs(float(yesterday_price) - float(day_before_price))*100/float(day_before_price)
print(difference)

if difference > 5 and float(yesterday_price) > float(day_before_price):
    coded_message = f"🔺{int(difference)}"
    title, description = fetch_news_stock()
    send_message(coded_message, title, description)
else:
    print("No News")
    coded_message = f"🔻{int(difference)}"
    title, description = fetch_news_stock()
    send_message(coded_message, title, description)

