import requests
import os

TEQUILA_ENDPOINT = 'https://api.tequila.kiwi.com/'
TEQUILA_API_KEY = os.environ['TEQUILA_API_KEY']

headers = {
    'apikey': TEQUILA_API_KEY,
    'Content-Type': 'application/json'
}


class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def get_destination_code(self, city_name):
        query = {"term": city_name, "location_types": "city"}
        response = requests.get(f'{TEQUILA_ENDPOINT}locations/query', headers=headers, params=query)
        response.raise_for_status()
        results = response.json()['locations']
        code = results[0]['code']
        return code
