import bot.sites.bestbuy_gigabyte as bbg
import bot.sites.bestbuy_nvidia as bbn
import bot.sites.bestbuy_test as bbtest

def scraper():
    bbg.check_availibility()
    bbn.check_availibility()
    bbtest.check_availibility()

    return
    