from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import time
import sys
import csv

path = "C:\\Coding1\\Coding\\python\\Automation\\chromedriver-win64\\chrome.exe"

url = "https://web.whatsapp.com/"

options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=C:\\Users\\aayus\\AppData\\Local\\Google\\Chrome for Testing\\User Data\\Default")
options.add_argument("profile-directory=Default") 
options.binary_location = path

driver = webdriver.Chrome(options)
driver.get(url)

time.sleep(20)
target = sys.argv[1]
text = sys.argv[2]
n = int(sys.argv[3])

contactpath = f"//span[contains(@title, '{target}')]"

wait = WebDriverWait(driver, 100)
contact = wait.until(EC.presence_of_element_located((By.XPATH, contactpath)))
contact.click()

time.sleep(5)

for i in range (0,n):
    wait = WebDriverWait(driver, 10)
    message_box = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[role='textbox'][contenteditable='true'][tabindex='10']")))
    message_box.click()
    message_box.send_keys(text)
    time.sleep(0.05)
    send_button = driver.find_element(by = "xpath",value= '//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div[2]/button')
    send_button.click()  

driver.quit()