#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from unittest import result
import data_manager
import flight_data
import flight_search

flight_info = data_manager.DataManager()
search_info = flight_search.FlightSearch()
flight_search_result = flight_data.FlightData()

sheet_data = flight_info.sheet_api()
city_list = []
for index in range(len(sheet_data)):
    if sheet_data[index]["iataCode"] == "":
        city_list.append(sheet_data[index]["city"])
# consider putting these two loops into their own class files
sheet_object_id = 2
for city in city_list:
    airport_code = search_info.citysearch(city)
    flight_info.edit_code(sheet_object_id, airport_code)
    sheet_object_id += 1

result_cities = flight_search_result.oneway_flight_search()

relevant_oneway_flights = {k: v for k,v in result_cities.items() if k in flight_info.relevant_cities}
if relevant_oneway_flights == {}:
    print("No oneway flights to desired cities in the next 6 months")
else:
    for k,v in relevant_oneway_flights.items():
        print(f"{k}: ${v}")