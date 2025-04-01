#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
api = DataManager()
flight = FlightSearch()
sheet_data = api.getapi()
print(sheet_data)
for i in sheet_data:
    iatacode = i["city"]
    iata = flight.get_iata_code(iatacode)
    i["iataCode"] = iata

    row_id = i["id"]
    api.update_iata_code(row_id, iata)

print(sheet_data)


