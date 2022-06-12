import json
import requests

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    search_url = "https://tequila-api.kiwi.com/locations/query"
    search_headers = {
        "accept": "application/json",
        "apikey": "{{API TOKEN}}",
    }

    def citysearch(self, city):
        response = (requests.get(url=self.search_url, headers=self.search_headers, params={"term": city, "location_types": "airport"})).json()
        return response["locations"][0]["code"]
        