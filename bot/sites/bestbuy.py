from bot.helpers import chromeHelper as chrome
from bs4 import BeautifulSoup
import bot.sites.links as link


def check_availibility(url):
    driver = chrome.chrome_driver()
    availible = False
    print(f'Accessing {url}')
    
    
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
        print('No correct element found')
        chrome.close(driver)
        return ""
    
   
    chrome.close(driver)

    print('Availible? ' + str(availible))
    print('Done!')

    if availible == True:
        return url
    else:
        return ""

def scraper():

    
    availible = []

    message = "Best Buy GPU(s) availible: "
    bestbuy_links = link.bestbuyLinks()
    for url in bestbuy_links:
        is_availible = check_availibility(url)

        if is_availible != "":
            availible.append(str(is_availible))

    if len(availible) != 0:
        for url in availible:
            print(f'{availible} {url}')
            message = message + f"{url} \n"
        return {'message': message, 'error': False}

    else:
        return False
 