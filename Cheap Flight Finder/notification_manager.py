import os
from twilio.rest import Client

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
twilio_nr = os.environ['TWILIO_NUMBER']
my_number = os.environ['MY_NUMBER']


class NotificationManager:
    def __init__(self):
        self.client = Client(account_sid, auth_token)

    def send_sms(self, price, departure_city, arrival_city, outbound_date, inbound_date):
        message = self.client.messages.create(
            body=f"Low price alert! Only {price}€ to fly from {departure_city} to {arrival_city}."
                 f"from {outbound_date} to {inbound_date}.",
            from_=twilio_nr,
            to=my_number
        )
