# Day 35 - exercises
# API authentication
import os
import requests
from twilio.rest import Client


parameters = {
    "lat": {{LAT}},
    "lon": {{LON}},
    "exclude": "current,minutely,daily,alerts",
    "appid": os.environ["OWM_API_TOKEN"],
}

api_url = "https://api.openweathermap.org/data/2.5/onecall"

response = requests.get(url=api_url, params=parameters)
response.raise_for_status()

weather_data = response.json()
hourly_weather_data = weather_data["hourly"][:12]

rain_today = False

for hour in hourly_weather_data:
    weather_code = int(hour["weather"][0]["id"])
    if weather_code < 600:
        rain_today = True

if rain_today == True:
    text_message = "It's going to rain in the next 12 hours. Pack an umbrella!"
else:
    text_message = "No rain forecasted in the next 12 hours. All clear!"


# Twilio API
twilio_sid = os.environ["TWILIO_SID"]
twilio_token = os.environ["TWILIO_TOKEN"]
twilio_number = os.environ["TWILIO_NUMBER"]

client = Client(twilio_sid, twilio_token)

message = client.messages \
                .create(
                     body=text_message,
                     from_=twilio_number,
                     to=os.environ["RECIPIENT_PHONE_NUMBER"]
                 )

print(message.sid)

