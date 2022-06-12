import json
import requests

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    sheet_url = "https://api.sheety.co/f16849ca4ad6901b130f707cd640040d/copyOfFlightDeals/prices"
    sheet_token = "{{API TOKEN}}"
    sheet_headers = f"Authorization: Bearer {sheet_token}"
    sheet_edit_url = "https://api.sheety.co/f16849ca4ad6901b130f707cd640040d/copyOfFlightDeals/prices/"

    relevant_cities = []

    def sheet_api(self):
        response = (requests.get(url=self.sheet_url)).json()
        for city in response["prices"]:
            self.relevant_cities.append(city["city"])
        return response["prices"]

    def edit_code(self, object_id, code):
        response = (requests.put(url=f"{self.sheet_edit_url}{object_id}", json={"price": {"iataCode": code}}))
        return response

    


