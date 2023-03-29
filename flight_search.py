import requests
from datetime import datetime, timedelta
import pprint

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
        self.return_from = (self.tomorrow_date + timedelta(7)).strftime('%d/%m/Y%')
        self.return_to = (self.tomorrow_date + timedelta(28)).strftime('%d/%m/%Y')


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
            'return_from': self.date_from,
            'return_to': self.return_to,
        }

        response = requests.get(f'{TEQUILA_ENDPOINT}v2/search', headers=headers, params=query)
        response.raise_for_status()
        results = response.json()
        price = [data['price'] for data in results['data']]
        # print(price)
        if len(price) > 0:
            return min(price)
        else:
            return 'N/A'
        # return code
