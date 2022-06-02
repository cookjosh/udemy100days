import requests
from pprint import pprint

sheet_data = requests.get("https://api.sheety.co/f16849ca4ad6901b130f707cd640040d/copyOfFlightDeals/prices")
pprint(sheet_data.text)