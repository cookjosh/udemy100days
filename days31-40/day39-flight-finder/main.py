#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
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
print(flight_info.relevant_cities) # This list is cities from the G sheet
print(result_cities) # This list needs to turn into a dict with flight price as value for each key
# These two lists need to be compared for matching values