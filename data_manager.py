import requests


data_url = 'https://api.sheety.co/bf1319166f794e5c89837c0e7c960e9d/copyOfFlightDeals/prices'
users_url = 'https://api.sheety.co/bf1319166f794e5c89837c0e7c960e9d/copyOfFlightDeals/users'

class DataManager:
    def __init__(self):
        self.sheety_url = data_url
        self.sheety_response = {}
        self.sheety_users_response = {}
        self.get_data()

    def get_data(self):
        sheety_data = requests.get(self.sheety_url)
        self.sheety_response = sheety_data.json()

    def update_iata(self, iata_code, n):
        update_para = {
            'price': {
                'iataCode': iata_code
            }
        }
        update_url = f"https://api.sheety.co/bf1319166f794e5c89837c0e7c960e9d/copyOfFlightDeals/prices/{n}"
        requests.put(url=update_url, json=update_para)

    def get_club_users(self):
        sheety_users = requests.get(users_url)
        self.sheety_users_response = sheety_users.json()
        return self.sheety_users_response




