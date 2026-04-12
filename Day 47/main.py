import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

load_dotenv()


url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", 
    "Accept-Encoding": "gzip, deflate, br, zstd", 
    "Accept-Language": "en-US,en;q=0.9", 
    "Priority": "u=0, i", 
    "Sec-Fetch-Dest": "document", 
    "Sec-Fetch-Mode": "navigate", 
    "Sec-Fetch-Site": "cross-site", 
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.4 Safari/605.1.15"
}
def send_price_alert(price: float) -> None:
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    email = os.getenv("MAIL_ID")
    password = os.getenv("MAIL_PASS")
    rec_mail = os.getenv("REC_MAIL")
    message = MIMEMultipart("alternative")
    message["Subject"] = "multipart test"
    message["From"] = email
    message["To"] = rec_mail

    html = f"""\
            <html>
            <body>
                <p>Hi,<br>
                Price Drop Alert<br>
                <a href="{url}">HotPot</a> 
                is now priced at {price}
                </p>
            </body>
            </html>
            """
    body = MIMEText(html, "html")

    message.attach(body)

    context = ssl.create_default_context()
    print(context, price)
    # print(context, price)
    # with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    #     server.login(email, password)
    #     server.sendmail(email, rec_mail, message.as_string())


def main():
    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, "html.parser")
    price = soup.find("span", class_="aok-offscreen")
    price = str(price).split(" $")[1].split(" with")[0]
    return float(price)


if __name__ == "__main__":
    price = main()
    print(price)
    if price < 100.00:
        send_price_alert(price)
    else:
        print("Price is high")
