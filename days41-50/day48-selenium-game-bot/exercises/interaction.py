from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "/Users/josh/Documents/chromedriver"
driver = webdriver.Chrome(executable_path = chrome_driver_path)

#driver.get("https://en.wikipedia.org/wiki/Main_Page")

# Clicking a link with Selenium
#article_count = driver.find_element(By.XPATH, "//*[@id='articlecount']/a[1]")
#article_count.click()

# Filling in a text field
#search_box = driver.find_element(By.NAME, "search")
#search_box.send_keys("python")
#search_box.send_keys(Keys.ENTER)

# Day 48 Challenge 2
# Go to test website and auto "sign-up" for newsletter
driver.get("http://secure-retreat-92358.herokuapp.com/")

first_name = "fake_first"
last_name = "fake_last"
fake_email = "fake.email@fake.com"

first_name_field = driver.find_element(By.NAME, "fName")
first_name_field.send_keys(first_name)
last_name_field = driver.find_element(By.NAME, "lName")
last_name_field.send_keys(last_name)
email_field = driver.find_element(By.NAME, "email")
email_field.send_keys(fake_email)

submit_button = driver.find_element(By.XPATH, "/html/body/form/button")
submit_button.click()








#driver.quit()