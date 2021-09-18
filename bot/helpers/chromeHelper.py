from selenium import webdriver
import os

def get_chrome_driver_path():
    if os.environ.get("LOCAL") == 'true':
        driver_path = os.getcwd() + '/local/chromedriver' 

    else:
        driver_path = os.environ.get("CHROMEDRIVER_PATH")
        print(driver_path)
    return driver_path

def chrome_driver():
    print("Setup for Driver")
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")

    # uncomment for deployment
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    
    
    driver = webdriver.Chrome(executable_path=get_chrome_driver_path(), chrome_options=chrome_options)
    print("Finished!")
    return driver

def close(driver):

    driver.quit()

