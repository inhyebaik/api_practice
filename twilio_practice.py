from twilio.rest import Client
import os

account_sid = os.environ['TWILIO_SID']
auth_token = os.environ['TWILIO_TOKEN']
my_num = "+16173197517"
twilio_num = "+16179348427"
test_num = "+15005550006"


client = Client(account_sid, auth_token)

message = client.messages.create(to=my_num, 
                                from_=twilio_num, 
                                body="Hey there")