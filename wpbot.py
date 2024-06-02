from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import time
import csv

path = "C:\Coding\python\Automation\chromedriver-win64\\chromedriver.exe"

url = "https://web.whatsapp.com/"
service = Service(executable_path= path)
driver = webdriver.Chrome(service = service)

driver.get(url)
time.sleep(45)
target = '"Aayuuuu"'

#Xpath = '//tagname[contains(@Attribute,'+ target +')]'
contactpath = '//span[contains(@title,'+ target +')]'


wait = WebDriverWait(driver, 100)
contact = wait.until(EC.presence_of_element_located((By.XPATH, contactpath)))
contact.click()

text = "hi"

time.sleep(2)
for i in range (0,10):
    message_box_path = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]'
    message_box = driver.find_element(by = "xpath",value= message_box_path)
    message_box.click()
    message_box.send_keys(text)
    send_path = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]'
    send_button = driver.find_element(by = "xpath",value= send_path)
    send_button.click()


driver.quit()