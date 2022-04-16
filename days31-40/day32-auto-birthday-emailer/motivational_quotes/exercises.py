# Day 32 - smtp and datetime modules practice
"""
import smtplib

my_email = {{YOUR_EMAIL}}
my_password = {{YOUR_EMAIL_PASSWORD}}
recipient_email = {{RECIPIENT_EMAIL}}

with smtplib.SMTP("smtp.gmail.com:587") as connection:
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs=recipient_email,
        msg="Subject:Hello\n\nBody Test, test, test"
    )
"""

import datetime as dt
now = dt.datetime.now()
# Pulling out specific attributes of initialized datetime object 'now'
month = now.month
year = now.year
day_of_week = now.weekday()

# Creating custom dt object with specified properties
date_of_birth = dt.datetime(year=1978, month=5, day=18)
print(date_of_birth)
