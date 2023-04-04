from twilio.rest import Client
import os

ACCOUNT_SID = os.environ["TWILIO_ACCOUNT_SID"]
AUTH_TOKEN = os.environ["TWILIO_AUTH_TOKEN"]
TWILIO_VIRTUAL_NUMBER = os.environ["TWILIO_VIRTUAL_NUMBER"]
TWILIO_VERIFIED_NUMBER = os.environ["TWILIO_VERIFIED_NUMBER"]


class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.client = Client(ACCOUNT_SID, AUTH_TOKEN)

    def send_message(self, message):
        message = self.client.messages.create(
            body=message,
            from_=f"{TWILIO_VIRTUAL_NUMBER}",
            to=f"{TWILIO_VERIFIED_NUMBER}"
        )
        print(message.sid)