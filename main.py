#This file will need to use the DataManager,FlightSearch, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from pprint import pprint
from flight_search import FlightSearch
from notification_manager import NotificationManager


sheet_flights = DataManager()

users_dict = sheet_flights.get_club_users()

flight_cheap_info = FlightSearch()

my_notify = NotificationManager(users_dict)

for city in sheet_flights.sheety_response['prices']:
    if city['iataCode'] == '':
        city_iata = flight_cheap_info.get_iatacode(city['city'])
        sheet_flights.update_iata(city_iata,  city['id'])

    cheapest_flight_dict = flight_cheap_info.get_cheapest(city['city'])

    print (cheapest_flight_dict)

# # Creating message for cheaper flights and then sending via message / mail

    if cheapest_flight_dict['price'] < city['lowestPrice']:
        my_notify.create_message(cheapest_flight_dict)
    else:
        pass




