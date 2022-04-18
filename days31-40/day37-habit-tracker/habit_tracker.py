# Day 37 Project - Habit Tracker
# Did not create functionality to use this without editing the code
# Simply used this to practice using requests methods


import datetime as dt
from turtle import up
import requests

now = dt.datetime.now()
today = now.strftime("%Y%m%d")

users_url = "https://pixe.la/v1/users"
users_data = {
    "token": "qccf38yWZujwn4TeFPsE6sVN",
    "username": "udemytest1",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# user_response = requests.post(url=users_url, json=users_data)

graph_url = f"https://pixe.la/v1/users/{users_data['username']}/graphs"
graph_data = {
    "id": "testgraph1",
    "name": "Test Graph",
    "unit": "commit",
    "type": "int",
    "color": "ajisai",
}
pixela_header = {
    "X-USER-TOKEN": users_data["token"]
}

# graph_response = requests.post(url=graph_url, headers=pixela_header, json=graph_data)

pixel_url = f"https://pixe.la/v1/users/{users_data['username']}/graphs/{graph_data['id']}"
pixel_data = {
    "date": today,
    "quantity": "10"
}

# pixel_response = requests.post(url=pixel_url, headers=pixela_header, json=pixel_data)

#Updating a pixel
update_pixel_url = f"https://pixe.la/v1/users/udemytest1/graphs/testgraph1/{today}"
update_pixel_data = {
    "quantity": "100",

}

# update_response = requests.put(url=update_pixel_url, headers=pixela_header, json=update_pixel_data)

#Delete a pixel
delete_response = requests.delete(url=update_pixel_url, headers=pixela_header)
print(delete_response.json())
