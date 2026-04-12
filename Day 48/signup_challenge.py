from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("http://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(By.XPATH, value="/html/body/form/input[1]")
first_name.send_keys("TestFirst")

last_name = driver.find_element(By.XPATH, value="/html/body/form/input[2]")
last_name.send_keys("TestLast")

email_address = driver.find_element(By.XPATH, value="/html/body/form/input[3]")
email_address.send_keys("test@test.com")

signup = driver.find_element(By.XPATH, value="/html/body/form/button")
signup.click()
