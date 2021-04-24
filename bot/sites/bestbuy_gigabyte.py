from bot.scraper import chromeHelper as chrome
from bs4 import BeautifulSoup

def html_write(source):
    file = open("testfile.html","w") 
    file.write(source)
    file.close()
    return

def check_availibility():
    driver = chrome.chrome_driver()
    print('into bestbuy.com gigabyte')
    page_source = driver.get("https://www.bestbuy.com/site/gigabyte-nvidia-geforce-rtx-3070-eagle-8gb-gddr6-pci-express-4-0-graphics-card/6437912.p?acampID=0&cmp=RMX&loc=Hatch&ref=198&skuId=6437912")

    html_write(driver.page_source)
   
    chrome.close(driver)
    print('done')

    return

    # get_soup = BeautifulSoup(page_source, 'html.parser')