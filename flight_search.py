import requests
from datetime import datetime, timedelta
from flight_data import FlightData

import os

TEQUILA_ENDPOINT = 'https://api.tequila.kiwi.com/'
TEQUILA_API_KEY = os.environ['TEQUILA_API_KEY']

headers = {
    'apikey': TEQUILA_API_KEY,
    'Content-Type': 'application/json'
}


class FlightSearch:
    def __init__(self):
        self.tomorrow_date = datetime.today() + timedelta(1)
        self.date_from = self.tomorrow_date.strftime('%d/%m/%Y')
        self.date_to = (self.tomorrow_date + timedelta(180)).strftime('%d/%m/%Y')
        self.min_stay = 7
        self.max_stay = 28
    #This class is responsible for talking to the Flight Search API.

    def get_destination_code(self, city_name):
        query = {"term": city_name, "location_types": "city"}
        response = requests.get(f'{TEQUILA_ENDPOINT}locations/query', headers=headers, params=query)
        response.raise_for_status()
        results = response.json()['locations']
        code = results[0]['code']
        return code

    def search_for_flights(self, departure_city, city_name):
        query = {
            'fly_from': departure_city,
            'fly_to': city_name,
            'max_stopovers': 0,
            'date_from': self.date_from,
            'date_to': self.date_to,
            'nights_in_dst_from': self.min_stay,
            'nights_in_dst_to': self.max_stay,
            'flight_type': 'round',
            'curr': 'USD'
        }

        response = requests.get(f'{TEQUILA_ENDPOINT}v2/search', headers=headers, params=query)
        response.raise_for_status()

        try:
            results = response.json()['data'][0]
        except IndexError:
            print(f'No flights found for {city_name}')
            return None

        flight_data = FlightData(
            price=results['price'],
            origin_city=results['cityFrom'],
            origin_airport=results['flyFrom'],
            destination_city=results['cityTo'],
            destination_airport=results['flyTo'],
            departure_date=results["route"][0]["local_departure"].split("T")[0],
            return_date=results["route"][1]["local_departure"].split("T")[0]
        )

        print(f'{flight_data.destination_city}: ${flight_data.price}')
        return flight_data
