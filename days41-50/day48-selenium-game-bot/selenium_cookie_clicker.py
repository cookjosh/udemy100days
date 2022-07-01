from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time


chrome_driver_path = "/Users/josh/Documents/chromedriver"
driver = webdriver.Chrome(executable_path = chrome_driver_path)

driver.get("http://orteil.dashnet.org/experiments/cookie/")
cookie_icon = driver.find_element(By.ID, "cookie")

game_on = True
while game_on:
    cookie_icon.click()
