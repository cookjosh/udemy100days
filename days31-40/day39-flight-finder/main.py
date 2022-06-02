#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import data_manager

flight_info = data_manager.DataManager()

sheet_data = flight_info.sheet_api()
for index in range(len(sheet_data)):
    if sheet_data[index]["iataCode"] == "":
        print("No city code")