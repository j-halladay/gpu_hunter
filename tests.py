import bot.sites.bestbuyTest as bb
import bot.helpers.twilioHelper as twilio


def siteResults():

    bb_message = bb.scraper()
    return [bb_message,]

def fullReport():
    site_results = siteResults()
    report = ""
    
    for result in site_results:
        if result != False:
            print('Found something! Writing Report!')
            


            print(str(result['message']))
            if result['error'] != True:
                report = report + f"{str(result['message'])} \n"
                
        else:
            print('Nothing found!')
            
    if report != "":
        twilio.send_sms(report)

print('Running test...')

fullReport()

print("stopping...")