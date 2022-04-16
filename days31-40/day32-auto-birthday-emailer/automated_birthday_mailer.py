# Day32 Project - Automated Birtday Emailer
# Take a CSV of people's birthdays
# If someone's birthday occurs on today's date, send an automated email
import datetime as dt
import pandas
import random
import smtplib

# Parse CSV for dates and create date string for today
today = dt.datetime.now()
today_day = today.day
today_month = today.month
if today.month < 10:
    today_month = str(f"0{today.month}")
if today.day < 10:
    today_day = str(f"0{today.day}")
today_date = f"{today_month}-{today_day}"

birthday_data = pandas.read_csv("birthdays.csv")
birthday_dict = birthday_data.to_dict(orient="records")

# Set up sender email
my_email = {{YOUR_EMAIL}}
my_password = {{YOUR_PASSWORD}}

# Check if today matches a birthday in the birthdays.csv
for person in birthday_dict:
    if int(person["month"]) < 10:
        modified_month = f"0{str(person['month'])}"
    else:
        modified_month = person["month"]
    if int(person["day"]) < 10:
        modified_day = f"0{str(person['day'])}"
    else:
        modified_day = person["day"]
    person_birthday = f"{modified_month}-{modified_day}"
    if person_birthday == today_date:
        # Pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
        file_number = str(random.randint(1, 3))
        with open(f"./letter_templates/letter_{file_number}.txt", "r") as template:
            template_data = template.read()
            template_data = template_data.replace("[NAME]", f"{person['name']}")
        with open(f"./letter_templates/letter_{file_number}.txt", "w") as template:
            template.write(template_data)
            recipient_email = person["email"]
            # Send the letter generated in step 3 to that person's email address.
            with smtplib.SMTP("smtp.gmail.com:587") as connection:
                connection.starttls()
                connection.login(user=my_email, password=my_password)
                connection.sendmail(
                    from_addr=my_email,
                    to_addrs=recipient_email,
                    msg=f"Subject:Happy Birthday!\n\n{template_data}"
                )
