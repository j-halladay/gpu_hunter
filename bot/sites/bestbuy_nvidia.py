from bot.scraper import chromeHelper as chrome
from bs4 import BeautifulSoup

def html_write(source):
    file = open("testfile.html","w") 
    file.write(source)
    file.close()
    return

def check_availibility():
    driver = chrome.chrome_driver()
    print('into bestbuy.com nvidia')
    driver.get("https://www.bestbuy.com/site/nvidia-geforce-rtx-3070-8gb-gddr6-pci-express-4-0-graphics-card-dark-platinum-and-black/6429442.p?skuId=6429442")

    html_write(driver.page_source)
   
    chrome.close(driver)
    print('done')

    return
    # get_soup = BeautifulSoup(page_source, 'html.parser')
