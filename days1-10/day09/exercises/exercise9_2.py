# Exercise 9.2 - Travel Log
# Purpose - define function that will take parameters, create a dictionary, and add to existing travel log list


travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

# My function below
def add_new_country(country_name, number_visits, cities_list):
    new_entry = {}
    new_entry["country"] = country_name
    new_entry["visits"] = int(number_visits)
    new_entry["cities"] = cities_list
    travel_log.append(new_entry)

#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)