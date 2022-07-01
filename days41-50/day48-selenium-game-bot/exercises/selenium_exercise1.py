# Day 48 exercise 1
# Use selenium to scrape info from upcoming events menu at python.org
# Create a dict with each event date and name

from selenium import webdriver
from selenium.webdriver.common.by import By


chrome_driver_path = "/Users/josh/Documents/chromedriver"
driver = webdriver.Chrome(executable_path = chrome_driver_path)

driver.get("https://www.python.org")

main_event_dict = {}
dict_index = 0

# uses range func to iterate through list item sequence
for i in range(1, 6):
    date_one = driver.find_element(By.XPATH, f"//*[@id='content']/div/section/div[2]/div[2]/div/ul/li[{i}]/time")
    event_one = driver.find_element(By.XPATH, f"//*[@id='content']/div/section/div[2]/div[2]/div/ul/li[{i}]/a")
    main_event_dict[dict_index] = {"time": date_one.text, "name": event_one.text}
    dict_index += 1

print(main_event_dict)

driver.quit()