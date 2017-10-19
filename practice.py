from twilio.rest import Client
import os

account_sid = os.environ['TWILIO_SID']
auth_token = os.environ['TWILIO_TOKEN']



client = Client(account_sid, auth_token)

message = client.messages.create(
        to=)