##################### Hard Starting Project ######################
import random
import smtplib
import datetime
import pandas as pd
EMAIL_ADDRESS = '<EMAIL>'
PASSWORD = "<Password>"

letter_templates = ['letter_1','letter_2','letter_3']
def send_email(mail_id, subject, body):
    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()

        connection.login(EMAIL_ADDRESS, PASSWORD)
        connection.sendmail(
            from_addr=EMAIL_ADDRESS,
            to_addrs=mail_id,
            msg=f"Subject: {subject}\n\n {body}"
        )
date = datetime.date.today()
today = (date.month, date.day)
data = pd.read_csv('birthdays.csv')
# birthday_dict = dict(zip(zip(data['month'], data['day']),data.index))
birthday_dict = {
    (data_row['month'], data_row['day']): data_row for (index, data_row) in data.iterrows()
}

if today in birthday_dict:
    name = birthday_dict[today]['name']
    with open(f"letter_templates/{random.choice(letter_templates)}.txt") as f:
        letter_template = f.read()
        letter = letter_template.replace("[NAME]",name)
        email_id = birthday_dict[today]['email']
        send_email(email_id, "Happy Birthday!!", letter)



