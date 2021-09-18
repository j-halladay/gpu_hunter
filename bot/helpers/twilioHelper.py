from twilio.rest import Client
import os
def send_sms(message):



    # the following line needs your Twilio Account SID and Auth Token
    client = Client(os.environ.get("TWILIO_SSID"), os.environ.get("TWILIO_AUTH_TOKEN"))

    # change the "from_" number to your Twilio number and the "to" number
    # to the phone number you signed up for Twilio with, or upgrade your
    # account to send SMS to any phone number
    client.messages.create(to=str(os.environ.get("RECIPIENT_PHONE")), 
                       from_=str(os.environ.get("TWILIO_PHONE")), 
                       body=str(message))
    error_message_sent = False