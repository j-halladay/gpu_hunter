from bot.scraper import chromeHelper as chrome
from bs4 import BeautifulSoup


# def html_write(source):
#     file = open("testfile.html","w") 
#     file.write(source)
#     file.close()
#     return

def check_availibility():
    driver = chrome.chrome_driver()
    availible = False

    

    print('into bestbuy.com gigabyte')
    url = "https://www.bestbuy.com/site/sony-85-classx900h-series-led-4k-uhd-smart-android-tv/6401211.p?skuId=6401211"
    
    driver.get(url)

    driver.implicitly_wait(10)
    
    try: 
        myDynamicElement = driver.find_element_by_css_selector("button.add-to-cart-button")

        # html_write(driver.page_source)
        page_source = driver.page_source
        soup = BeautifulSoup(page_source, 'html.parser')
        inner_text = soup.find('button', attrs={'class': 'add-to-cart-button'}).text
        print('Inner text: ' + inner_text)
        if inner_text == 'Add to Cart':
            availible = True


    except:
        print('no element found')
        chrome.close(driver)
        return False
    
   
    chrome.close(driver)

    print('Availible? ' + str(availible))
    print('Done!')

    if availible == True:
        return url
    else:
        return ""