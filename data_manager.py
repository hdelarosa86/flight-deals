import requests
from requests.auth import HTTPBasicAuth
import os

SHEETY_ENDPOINT = os.environ['SHEETY_ENDPOINT']
BASIC_AUTH = HTTPBasicAuth(os.environ['AUTH_USERNAME'], os.environ['AUTH_PASS'])


class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.flight_data_list = None

    def fetch_flight_data(self):
        response = requests.get(SHEETY_ENDPOINT, auth=BASIC_AUTH)
        data = response.json()
        self.flight_data_list = data['prices']

        return self.flight_data_list

    def put_flight_data(self):
        for city in self.flight_data_list:
            new_data = {
                'price': {
                    'iataCode': city['iataCode'],
                    'lowestPrice': city['lowestPrice']
                }
            }
            requests.put(f'{SHEETY_ENDPOINT}/{city["id"]}', auth=BASIC_AUTH, json=new_data)
