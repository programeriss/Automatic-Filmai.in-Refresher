from seleniumwire import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import json
import os
import sys
import pickle
from requests import Session
from Screenshot import Screenshot_Clipping

chromeOptions = Options()
chromeOptions.add_argument('--headless') # comment if you want to see the browser window visually
chromeOptions.add_argument("--no-sandbox")
chromeOptions.add_argument("--window-size=1280,720")
chromeOptions.add_argument('--disable-gpu')
chromeOptions.add_argument('--disable-dev-shm-usage')
chromeOptions.add_argument('--disable-web-security')
chromeOptions.add_argument('-–allow-file-access-from-files')
chromeOptions.add_argument('--disable-site-isolation-trials')

caps = DesiredCapabilities.CHROME
caps['goog:loggingPrefs'] = {'performance': 'ALL'}

browser = webdriver.Chrome(executable_path="./chromedriver", options=chromeOptions, desired_capabilities=caps)

print("STARTING")

browser.get("http://37.221.162.250/index.php?do=login")

print("IN PROGRESS")

time.sleep(10)

print("IN PROGRESS")

inputElement = browser.find_element_by_id("login_append")
inputElement.send_keys('username') # enter your filmai.in username here

time.sleep(2)

inputElement = browser.find_element_by_id("password_append")
inputElement.send_keys('password') # enter you filmai.in password here

time.sleep(2)
inputElement.send_keys(Keys.ENTER)

print("IN PROGRESS")

time.sleep(5)

element = browser.find_elements_by_class_name("ptsplus")
element[0].click()

print("IN PROGRESS")

time.sleep(10)
ob=Screenshot_Clipping.Screenshot()
ob.full_Screenshot(browser, save_path=r'.', image_name='page_source.png')

print("DONE")
browser.quit()
