import requests
import smtplib
from datetime import datetime

MY_LAT = 37.5616008 # Your latitude
MY_LONG = -122.32454 # Your longitude

# Setup email
my_email = {{YOUR_EMAIL}}
my_password = {{YOUR_PASSWORD}}

# Check ISS position and if our position is within +5 or -5 degrees of that.
def current_iss_position():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if iss_latitude in range(MY_LAT - 5, MY_LAT + 6) and iss_longitude in range(MY_LONG - 5, MY_LONG + 6):
        return True
current_iss_position()

if current_iss_position() == True:

    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = (int(data["results"]["sunrise"].split("T")[1].split(":")[0])) - 8 # subtractions for Pacific time from UTC
    sunset = (int(data["results"]["sunset"].split("T")[1].split(":")[0])) - 8

    time_now = (datetime.now()).hour

    if sunrise >= time_now or sunset <= time_now:
        with smtplib.SMTP("smtp.gmail.com:587") as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=my_email,
                msg=f"Look Up!\n\nThe ISS is passing overhead!"
            )

# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



