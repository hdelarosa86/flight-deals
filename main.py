from data_manager import DataManager
from flight_search import FlightSearch
from pprint import pprint

data_manager = DataManager()

sheet_data = data_manager.fetch_flight_data()

for row in sheet_data:
    if row['iataCode'] == '':
        flight_search = FlightSearch()
        destination_code = flight_search.get_destination_code(row['city'])
        row['iataCode'] = destination_code
data_manager.flight_data_list = sheet_data
data_manager.put_flight_data()



