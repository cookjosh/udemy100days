import datetime
import requests
from dateutil.relativedelta import relativedelta


class FlightData:
    #This class is responsible for structuring the flight data.
    from_date = datetime.date.today()
    to_date = from_date + relativedelta(months=+6)
    flight_url = "https://tequila-api.kiwi.com/v2/search"
    flight_headers = {
        "accept": "application/json",
        "apikey": "pbjyPOypPVvAot8MBPJHqDby7jO_WNAC",
    }
    flight_data = {
        "fly_from": "LON",
        "date_from": from_date.strftime("%d/%m/%Y"),
        "date_to": to_date.strftime("%d/%m/%Y"),
        "flight_type": "oneway",
        "curr": "GBP",
    }
    

    def oneway_flight_search(self):
        response = (requests.get(url=self.flight_url, headers=self.flight_headers, params=self.flight_data)).json()
        oneway_list = response["data"]
        oneway_destinations = {destination["cityTo"]: destination["price"] for destination in oneway_list} # not sure price is the correct piece of data but whatever
        #destination_set = set(oneway_destinations)
        #unique_oneway_list = list(destination_set)
        #return (unique_oneway_list)
        return oneway_destinations

