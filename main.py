from data_manager import DataManager
from flight_search import FlightSearch

data_manager = DataManager()
flight_search = FlightSearch()
sheet_data = data_manager.fetch_flight_data()

for row in sheet_data:

    if row['iataCode'] == '':
        destination_code = flight_search.get_destination_code(row['city'])
        row['iataCode'] = destination_code

data_manager.flight_data_list = sheet_data
data_manager.put_flight_data()

for destination in sheet_data:
    destination_data = flight_search.search_for_flights('NYC', destination['iataCode'])

    if destination_data is None:
        destination['price'] = 'N/A'
    else:
        destination['price'] = destination_data['price']

data_manager.flight_data_list = sheet_data
data_manager.put_flight_data()