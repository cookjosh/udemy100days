# Day 32 - automated motivational quote emailer
# Use datetime to see if today is Monday
# If so, choose a random motivational quote from txt file
# Send to email

import datetime as dt
import random
import smtplib


# Setup datetime monitor to see if today is Monday
today = dt.datetime.now()
day_of_week = today.weekday()

# Create mailer with source and dest accounts
my_email = {{YOUR_EMAIL}}
my_password = {{YOUR_EMAIL_PASSWORD}}
recipient_email = {{RECIPIENT_EMAIL}}

if day_of_week == 0:
    # open txt file of quotes and select random quote
    with open(file="./quotes.txt") as quote_file:
        lines = quote_file.read().splitlines()
        random_quote = random.choice(lines)
    # use smtp to send email to recipient
    with smtplib.SMTP("smtp.gmail.com:587") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=recipient_email,
            msg=f"Subject:Today's Motivational Quote\n\nDear You,\n\n{random_quote}\n\nHave a wonderful week!"
        )

