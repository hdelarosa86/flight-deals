from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

data_manager = DataManager()
flight_search = FlightSearch()
sheet_data = data_manager.fetch_flight_data()
notification_manager = NotificationManager()

for row in sheet_data:

    if row['iataCode'] == '':
        destination_code = flight_search.get_destination_code(row['city'])
        row['iataCode'] = destination_code

data_manager.flight_data_list = sheet_data

for destination in sheet_data:
    destination_data = flight_search.search_for_flights('NYC', destination['iataCode'])

    if destination_data is not None and destination_data.price < destination["lowestPrice"]:
        notification_manager.send_message(
            message=f"Low price alert! Only ${destination_data.price} to fly "
                    f"from {destination_data.origin_city}-{destination_data.origin_airport} to "
                    f"{destination_data.destination_city}-{destination_data.destination_airport}, "
                    f"from {destination_data.departure_date} to {destination_data.return_date}."
        )

    if destination_data is not None:
        destination['lowestPrice'] = destination_data.price
    else:
        destination['lowestPrice'] = 'N/A'

data_manager.flight_data_list = sheet_data
data_manager.put_flight_data()
