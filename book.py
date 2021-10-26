import os
import re
import json
import time
import requests

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

long_wait_sec = 5
short_wait_sec = 0.5
page = "https://www.shh.org.tw/OldShhorg/shhreg1/UI/C/C10200.aspx?ok=O&od=1101030&dcode=AA&sno=1&droom=01A68&doc=15602"
national_id = "Fxxxxxxxxx"
birthday = "0yymmdd" # 100/10/10 => 1001010

if __name__ == "__main__":
    DRIVER_PATH = "/Users/jyhsia/homebrew/bin/chromedriver"
    options = webdriver.ChromeOptions()
    options.add_argument(r"--user-data-dir=C:\\/Applications/Google Chrome.app/Contents/MacOS/Google Chrome")
    driver = webdriver.Chrome(executable_path=DRIVER_PATH, chrome_options=options)

    driver.get(page)
    time.sleep(long_wait_sec)

    try:
        driver.switch_to.alert.accept()
    except:
        print("No alert!")

    # Confirm not the firt time
    driver.find_element_by_id("ContentPlaceHolder1_rbl_fvry_0").click()
    driver.find_element_by_id("ContentPlaceHolder1_ibtn_confirm0").click()
    time.sleep(short_wait_sec)

    # Fill national id
    elem = driver.find_element_by_id("ContentPlaceHolder1_txt_idno_R")
    elem.send_keys(national_id)
    time.sleep(short_wait_sec)


    # Fill birthday
    elem = driver.find_element_by_id("ContentPlaceHolder1_txt_birthdayR")
    elem.send_keys(birthday)
    time.sleep(short_wait_sec)


    # Confirm
    driver.find_element_by_id("ContentPlaceHolder1_ibtn_confirm").click()
    time.sleep(short_wait_sec)

    try:
        driver.switch_to.alert.accept()
    except:
        print("No alert!")
