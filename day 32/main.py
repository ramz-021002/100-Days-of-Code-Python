import smtplib
import random
import datetime as dt
EMAIL_ADDRESS = '<EMAIL>'
PASSWORD = "<Password>"

def send_email(subject, body):
    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()

        connection.login(EMAIL_ADDRESS, PASSWORD)
        connection.sendmail(
            from_addr=EMAIL_ADDRESS,
            to_addrs="<to email>",
            msg=f"Subject: {subject}\n\n {body}"
        )

def get_quote():
    with open('quotes.txt', 'r') as quotes:
        all_quote = quotes.readlines()
        return random.choice(all_quote)

def main():
    now = dt.datetime.now()
    day = now.weekday()

    if day == 4:
        send_email("Quote for the day", get_quote())


main()