from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("http://ozh.github.io/cookieclicker/")



time.sleep(2)
try:
    # Select English language
    language_button = driver.find_element(by=By.ID, value="langSelect-EN")
    print("Found language button, clicking...")
    language_button.click()
    time.sleep(1)
except NoSuchElementException:
    print("Language selection not found")
    
item_ids = [f"product{i}" for i in range(18)]

def cookieClicker():
    cookie_clicker = driver.find_element(By.ID, value="bigCookie")
    time_end = time.time() + 10
    while time.time() < time_end:
        cookie_clicker.click()

def store():    
    raw_cookie_text = driver.find_element(By.ID, value='cookies').text.split(" ")[0]
    cookie_count = int("".join(ch for ch in raw_cookie_text if ch.isdigit()) or 0)
    print(cookie_count)
    
    products = driver.find_elements(by=By.CSS_SELECTOR, value="div[id^='product']")
    best_item = None
    for product in reversed(products):  # Start from most expensive (bottom of list)
        # Check if item is available and affordable (enabled class)
        if "enabled" in product.get_attribute("class"):
            best_item = product
            break
    
    if best_item:
        best_item.click()
        print(f"Bought item: {best_item.get_attribute('id')}")

five_minutes = time.time() + 60 * 5
while True:
    cookieClicker()
    store()
    
    if time.time() > five_minutes:
        try:
            cookies_element = driver.find_element(by=By.ID, value="cookies")
            print(f"Final result: {cookies_element.text}")
        except NoSuchElementException:
            print("Couldn't get final cookie count")
        break
    