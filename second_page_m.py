#! usr/bin/venv/python3

# importing necessary libraries
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC  
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import urllib.request
# self wrote Modules and Packages  
from HTMLTagsId import TagsId # HTML Tags
from DataInputs import UserInputs # Inputs that user should enter

# Functions 
def chrome_location(chrome_location):
    return chrome_location
def second_page_data_finding_entring(
    url: str, ncode: str, phone: str, bday: str, bmonth: str, byear: str,
    mday: str, mmonth: str, myear: str, city: str , captchf2: str, sleep_1: int, sleep_2: int):
    # second page of website signup 
    try:
        # Open the signup page
        driver.get(url)
        time.sleep(sleep_1)

        # Find the form fields and input data
        national_field = driver.find_element(By.NAME, ncode)
        phone_field = driver.find_element(By.NAME, phone)
        birth_day_field = driver.find_element(By.NAME, bday)
        birth_month_field = driver.find_element(By.NAME, bmonth)
        birth_year_field = driver.find_element(By.NAME, byear)
        marriage_day_field = driver.find_element(By.NAME, mday)
        marriage_month_field = driver.find_element(By.NAME, mmonth)
        marriage_year_field = driver.find_element(By.NAME, myear)
        city_field = driver.find_element(By.NAME, city)
        global captcha_field # set to global cuz second page captcha solvers uses it
        # captcha_field = driver.find_element(By.NAME, captchf2) 

        # Input the data
        national_field.send_keys(UserInputs_data.national_code)
        phone_field.send_keys(UserInputs_data.phone_number)
        birth_day_field.send_keys(UserInputs_data.birth_day)
        birth_month_field.send_keys(UserInputs_data.birth_month)
        birth_year_field.send_keys(UserInputs_data.birth_year)
        marriage_day_field.send_keys(UserInputs_data.marriage_day)
        marriage_month_field.send_keys(UserInputs_data.marriage_month)
        marriage_year_field.send_keys(UserInputs_data.marriage_year)
        city_field.send_keys(UserInputs_data.city)
        time.sleep(sleep_2)
    except Exception as e:
        print(f"something went wrong find and enter level: {e}")
def second_page_captcha_solver():
    time.sleep(5)
    captcha_image_element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, TagsId.captcha_id_page2)))
    
    captcha_image_element = driver.find_element(By.ID, TagsId.captcha_id_page2)

    # Get the source URL of the captcha image
    captcha_image_url = captcha_image_element.get_attribute('src')

    # Download the captcha image
    urllib.request.urlretrieve(captcha_image_url, '/home/hasan/Desktop/py/Automated-VECBI/captchas/captcha_image.jpg')

    print("Captcha image downloaded successfully.")
    
    driver.quit()
    # captcha_field.send_keys(captchavaluep2)

def second_page_sumbit_end(submitf1: str):
    try:
        # Submit the form
        submit_button = driver.find_element(By.NAME, submitf1)
        submit_button.click()

        # Wait for the signup process to complete (you might need to adjust the wait time)
        WebDriverWait(driver, 10).until(EC.url_changes(TagsId.url))

    except Exception:
        print("something went wrong")

    finally:
        # Close the browser window
        driver.quit()

# UserInputs_data class -> instance creating
UserInputs_data = UserInputs()    

# getting the chrome location
Chrome_Location_Res = chrome_location('/home/hasan/Desktop/py/Automated-VECBI/needed_files/chromedriver')


# service and driver
service = Service(executable_path=Chrome_Location_Res)
driver = webdriver.Chrome(service=service)
