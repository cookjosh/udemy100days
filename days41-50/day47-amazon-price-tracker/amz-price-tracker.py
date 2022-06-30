import lxml
import os
import requests
import smtplib
from bs4 import BeautifulSoup

product_url = "https://www.amazon.com/Garmin-Forerunner-Premium-Triathlon-Smartwatch/dp/B07QTVMWVL/ref=sr_1_3?crid=1AROUTO7HDWD3&keywords=garmin+forerunner+945&qid=1656354276&sprefix=Garmin+forerunner+9%2Caps%2C932&sr=8-3"
headers = {
    "Accept-Language": "en-us",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15",
}

floor_price = 410.00

# --- BeautifulSoup to get current price info --- #
response = requests.get(url=product_url, headers=headers)
soup = BeautifulSoup(response.text, "lxml")
item_price = (soup.find(name="span", class_="a-offscreen")).text
item_float_price = float(item_price.replace("$", ""))

if item_float_price < floor_price:
    sender = os.environ.get("SENDER_EMAIL")
    recipient = os.environ.get("RECIPIENT_EMAIL")
    message = f"""From: {sender}
    To: {recipient}
    Subject: Garmin Forerunner Alert!
    
    The current price of the Garmin Forerunner 945 is ${floor_price}!
    Go to {product_url} to purchase!"""
    # --- SMTP to send email notification --- #
    try:
        smtpObj = smtplib.SMTP("smtp.gmail.com", port=587)
        smtpObj.sendmail(sender, recipient, message)
        print("Email sent!")
    except smtplib.SMTPException:
        print("Error sending email!")