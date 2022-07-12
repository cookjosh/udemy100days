from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time


chrome_driver_path = "/Users/josh/Documents/chromedriver"
driver = webdriver.Chrome(executable_path = chrome_driver_path)

driver.get("http://orteil.dashnet.org/experiments/cookie/")
cookie_icon = driver.find_element(By.ID, "cookie")

# Prices of upgrades
# Refactor this to be a loop that pulls from list of upgrades
# and inserts into find_element and creates price variable
cursor_info = driver.find_element(By.XPATH, "//*[@id='buyCursor']/b")
cursor_price = (cursor_info.text).split("- ", 1)[1]

grandma_info = driver.find_element(By.XPATH, "//*[@id='buyGrandma']/b")
grandma_price = (grandma_info.text).split("- ", 1)[1]

factory_info = driver.find_element(By.XPATH, "//*[@id='buyFactory']/b")
factory_price = (factory_info.text).split("- ", 1)[1]

mine_info = driver.find_element(By.XPATH, "//*[@id='buyMine']/b")
mine_price = (mine_info.text).split("- ", 1)[1]

shipment_info = driver.find_element(By.XPATH, "//*[@id='buyShipment']/b")
shipment_price = (shipment_info.text).split("- ", 1)[1]

alchemy_info = driver.find_element(By.XPATH, "//*[@id='buyAlchemy lab']/b")
alchemy_price = (alchemy_info.text).split("- ", 1)[1]

portal_info = driver.find_element(By.XPATH, "//*[@id='buyPortal']/b")
portal_price = (portal_info.text).split("- ", 1)[1]

time_machine_info = driver.find_element(By.XPATH, "//*[@id='buyTime machine']/b")
time_machine_price = (time_machine_info.text).split("- ", 1)[1]


#def upgrades():



"""
game_on = True
while game_on:
    cookie_icon.click()
"""