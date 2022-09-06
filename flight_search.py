import requests
import datetime as dt

API_KEY = '7C_Pg8lzPzRXNrAjVD7ExM6UDSXLu_Fq'
END_POINT = 'https://tequila-api.kiwi.com/v2/search'
LOC_POINT = 'https://tequila-api.kiwi.com/locations/query'

FLY_FROM = 'DEL'

today_date = dt.datetime.now()
FROM_DATE = today_date.strftime('%d/%m/%Y')

TO_DATE_RAW = today_date + dt.timedelta(days=2)
TO_DATE = TO_DATE_RAW.strftime('%d/%m/%Y')


kiwi_headers = {
            'apikey': API_KEY
        }


class FlightSearch:
    def __init__(self):
        self.new_price_list = []

    def get_cheapest(self, city_iata):

        kiwi_parameters = {
                'fly_from': FLY_FROM,
                'fly_to': city_iata,
                'date_from': str(FROM_DATE),
                'date_to': str(TO_DATE),
                'nights_in_dst_from': 6,
                'nights_in_dst_to': 8,
                'max_sector_stopovers': 0,
                'curr': 'INR',
                }
        response = requests.get(url=END_POINT, params=kiwi_parameters, headers=kiwi_headers)

        try:
            output = response.json()
            return output['data'][0]
        except IndexError:
            kiwi_parameters = {
                'fly_from': FLY_FROM,
                'fly_to': city_iata,
                'date_from': str(FROM_DATE),
                'date_to': str(TO_DATE),
                'nights_in_dst_from': 6,
                'nights_in_dst_to': 8,
                'max_sector_stopovers': 1,
                'curr': 'INR',
            }
            response = requests.get(url=END_POINT, params=kiwi_parameters, headers=kiwi_headers)
            output = response.json()
            # return output['data'][0]

    def get_iatacode(self, search_id):
        loc_params = {
            'term': search_id
        }
        response = requests.get(url=LOC_POINT, params=loc_params, headers=kiwi_headers)
        iata_response = response.json()
        return iata_response['locations'][0]['code']

