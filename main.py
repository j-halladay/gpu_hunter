import bot.scraper.scraper as scraper
import bot.sites.bestbuy_test as bbtest
__author__ = "j_halladay"

if __name__ == '__main__':
    print('Starting...')
    x = 2
    error_message_sent = False
    while x != 1:


        scraped_data = scraper.scraper()
        if scraped_data != False:
            print('Found something! Sending Report!')
            
            if scraped_data['error'] == True:
                if error_message_sent == False:
                    error_message_sent = True
            print(str(scraped_data['message']))
            scraper.send_sms(str(scraped_data["message"]))
        else:
            print('Nothing found!')
            # uncomment scraper.send_sms() for production

           
        sleep(1200)