import bot.sites.bestbuy as bb
from twilio.rest import Client
import os


def scraper():

    bb_urls = ["https://www.bestbuy.com/site/gigabyte-nvidia-geforce-rtx-3070-eagle-8gb-gddr6-pci-express-4-0-graphics-card/6437912.p?acampID=0&cmp=RMX&loc=Hatch&ref=198&skuId=6437912",
                "https://www.bestbuy.com/site/nvidia-geforce-rtx-3070-8gb-gddr6-pci-express-4-0-graphics-card-dark-platinum-and-black/6429442.p?skuId=6429442",
                
                ]
    # error_urls = ["https://www.google.com"]
    # test_urls = ["https://www.bestbuy.com/site/sony-85-classx900h-series-led-4k-uhd-smart-android-tv/6401211.p?skuId=6401211",]
    availible = []

    message = "GPU(s) availible: "

    for url in test_urls:
        is_availible = bb.check_availibility(url)
        if is_availible == "Error":
            return {'message': f"Error: Cannot find Any Button in {url}", 'error': True}
        if is_availible != "":
            availible.append(str(is_availible))
            #enable in production 
            send_sms(f"Immediate Action, buy GPU now {str(url)}")

    if len(availible) != 0:
        for url in availible:
            print(f'{availible} {url}')
            message = message + f"{url} \n"
        return {'message': message, 'error': False}

    else:
        return False


def send_sms(message):



# the following line needs your Twilio Account SID and Auth Token
    client = Client(os.environ.get("TWILIO_SSID"), os.environ.get("TWILIO_AUTH_TOKEN"))

# change the "from_" number to your Twilio number and the "to" number
# to the phone number you signed up for Twilio with, or upgrade your
# account to send SMS to any phone number
    client.messages.create(to=str(os.environ.get("RECIPIENT_PHONE")), 
                       from_=str(os.environ.get("TWILIO_PHONE")), 
                       body=str(message))
        




    

    