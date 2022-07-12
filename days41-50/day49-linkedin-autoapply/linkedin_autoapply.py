# Day 49 - Automated Job Apply on LinkedIn
# Not currently open to work so will "Save" jobs instead of applying

import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

linkedin_username = os.environ.get("LINKEDIN_USERNAME")
linkedin_password = os.environ.get("LINKEDIN_PASSWORD")

chrome_driver_path = "/Users/josh/Documents/chromedriver"
driver = webdriver.Chrome(executable_path = chrome_driver_path)
driver.get("https://www.linkedin.com/jobs/search/?f_AL=true&f_E=2%2C3&f_WT=1%2C2&geoId=90000084&keywords=infrastructure%20engineer&location=San%20Francisco%20Bay%20Area&sortBy=R")

# Handle LinkedIn login
time.sleep(5)
login_button = driver.find_element(By.XPATH, "/html/body/div[1]/header/nav/div/a[2]")
login_button.click()
time.sleep(5)
username_field = driver.find_element(By.ID, "username")
username_field.send_keys(linkedin_username)
password_field = driver.find_element(By.ID, "password")
password_field.send_keys(linkedin_password)
signin_button = driver.find_element(By.XPATH, "//*[@id='organic-div']/form/div[3]/button")
signin_button.click()

# Save first job listed
time.sleep(5)
save_button = driver.find_element(By.CLASS_NAME, "jobs-save-button")
save_button.click()