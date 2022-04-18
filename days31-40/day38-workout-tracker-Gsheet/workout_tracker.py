# Day 38 Project - Workout Tracker in Google Sheets
# Use Nutritionix language API to interpret user input of exercise
# Use Sheety API to write Nutritionix data to a Google Sheet

import datetime as dt
import os
import requests

today = dt.datetime.now().strftime("%m/%d/%Y")
time = str(dt.datetime.now().time()).split(".", 1)


nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

nutritionix_headers = {
    "x-app-id": os.environ["NUTRITIONIX_APP_ID"],
    "x-app-key": os.environ["NUTRITIONIX_API_TOKEN"],
    "x-remote-user-id": "0",
}

nutritionix_data = {
    "query": input("Describe your exercise: "),
    "gender": "male",
    "weight_kg": 92.98,
    "height_cm": 180.34,
    "age": 34,
}

nutritionix_response = requests.post(url=nutritionix_endpoint, headers=nutritionix_headers, json=nutritionix_data)
nutritionix_data = nutritionix_response.json()["exercises"]


sheety_url = "https://api.sheety.co/f16849ca4ad6901b130f707cd640040d/workouts/sheet1"
sheety_data = {
    "sheet1": {
        "date": today,
        "time": time[0],
        "exercise": nutritionix_data[0]["name"],
        "duration": int(nutritionix_data[0]["duration_min"]),
        "calories": nutritionix_data[0]["nf_calories"],
    }
}
sheety_header = {
    "Authorization": f"Bearer {os.environ['SHEETY_API_TOKEN']}",
}

sheety_response = requests.post(url=sheety_url, headers=sheety_header, json=sheety_data)
print(sheety_response.json())