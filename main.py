import bot.scraper as scraper

__author__ = "j_halladay"

if __name__ == '__main__':
    print('Starting...')

    scraper.fullReport()
    # if scraped_data != False:
    #     print('Found something! Sending Report!')
        
    #     # if scraped_data['error'] == True:
    #     #     if error_message_sent == False:
    #     #         error_message_sent = True
    #     print(str(scraped_data['message']))
    #     twilio.send_sms(str(scraped_data["message"]))
    # else:
    #     print('Nothing found!')
        # uncomment scraper.send_sms() for production

    print("Stopping...")

           
