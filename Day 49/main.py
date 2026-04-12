from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from dotenv import load_dotenv

load_dotenv()

url = os.getenv("GYM_URL")
email = os.getenv("ACCOUNT_EMAIL")
password = os.getenv("ACCOUNT_PASSWORD")

user_data_dir = os.path.join(os.getcwd(), "chrome_profile")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")

driver = webdriver.Chrome(options=chrome_options)

def login():
    driver.get(f"{url}/login")

    email_input = driver.find_element(By.ID, value='email-input')
    email_input.send_keys(email)

    password_input = driver.find_element(By.ID, value='password-input')
    password_input.send_keys(password)

    login_button = driver.find_element(By.ID, value='submit-button')
    login_button.click()


login()