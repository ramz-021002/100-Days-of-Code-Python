import os
from twilio.rest import Client



class NotificationManager:
    pass
    # def __init__(self):
    #     self.client = Client(os.environ['TWILIO_SID'], os.environ["TWILIO_AUTH_TOKEN"])
    #

    # def send_whatsapp(self, message_body):
    #     message = self.client.messages.create(
    #         from_=f'whatsapp:{os.environ["TWILIO_WHATSAPP_NUMBER"]}',
    #         body=message_body,
    #         to=f'whatsapp:{os.environ["TWILIO_VERIFIED_NUMBER"]}'
    #     )
    #     print(message.sid)
