from datetime import datetime
import requests
import smtplib

# Basic REST API request practice
"""
response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status() # raises error if api call was unsuccessful

data = response.json()
print(data)
"""

# sunrise-sunset REST API, practice with parameters
today = datetime.today().strftime("%Y-%m-%d")

parameters = {
    "lat": 37.5616008,
    "lng": -122.32454,
    "date": today,
    "formatted": 0,
}

response = requests.get(
    url="https://api.sunrise-sunset.org/json",
    params=parameters,
    verify=False
)
response.raise_for_status()
response_results = (response.json())["results"]
sunrise_time = response_results["sunrise"]
sunset_time = response_results["sunset"]
print(sunrise_time, sunset_time)
