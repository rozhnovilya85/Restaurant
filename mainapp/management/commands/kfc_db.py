import time

from django.core.management import BaseCommand
import json
import requests
from geopy.geocoders import Nominatim

from mainapp.models import RestaurantDB


class Command(BaseCommand):

    def handle(self, *args, **options):
        # all_rest = {}
        # url = 'https://burgerkingrus.ru/order-app/api/v1/restaurants/search'
        # response = requests.get(url)
        # # data = response.json()
        # data = json.loads(response.text)
        # all_rest = data['response']
        #
        # for item in all_rest:
        #     geolocator = Nominatim(user_agent="geoapiExercises")
        #     location = geolocator.reverse(item['latitude'] + "," + item['longitude'])
        #     address = location.raw['address']
        #     _city = address.get('city', '')
        #
        #     rest_data = RestaurantDB(
        #         name_rest=item['name'],
        #         city=_city,
        #         address=item['address']
        #     )
        #     rest_data.save()


        # all_rest = {}
        # url = 'https://vkusnoitochka.ru/api/restaurants'
        # response = requests.get(url)
        # # data = response.json()
        # data = json.loads(response.text)
        # all_rest = data['restaurants']
        # list_id = list()
        # for item in all_rest:
        #     list_id.append(str(item['id']))
        #
        #
        # list_rest = list()
        # url_1 = 'https://vkusnoitochka.ru/api/restaurant/'
        # for a in list_id:
        #     response = requests.get(url_1 + a)
        #     data_r = json.loads(response.text)
        #     rest = data_r['restaurant']
        #     print(rest)
        #     list_rest.append(rest)
        #     time.sleep(0.2)
        # print(list_rest)

        url = 'https://api.kfc.digital/api/store/v2/store.get_restaurants'
        response = requests.get(url)
        data = json.loads(response.text)['searchResults']
        list_error = list()
        for item in data:
            try:
                rest_data = RestaurantDB(
                        name_rest=item['storePublic']['title']['ru'],
                        city=item['storePublic']['contacts']['city']['ru'],
                        address=item['storePublic']['contacts']['streetAddress']['ru'],
                        timezone=item['storePublic']['timeZone'],
                        brand=item['storePublic']['brand'],
                        is_active='True'
                    )
                rest_data.save()
            except:
                list_error.append(item)
        with open('log_kfc.txt', 'w') as file:
            file.writelines(str(list_error))























        # print(type(data))
        # all_rest = data['response'][600]['address']
        # print(all_rest)
        # # for item in data['response']:
        # #     print(item)
        #
        # geolocator = Nominatim(user_agent="geoapiExercises")
        # location = geolocator.reverse(data['response'][600]['latitude'] + "," + data['response'][600]['longitude'])
        # print(location)
        # address = location.raw['address']
        # city = address.get('city', '')
        # state = address.get('state', '')
        # country = address.get('country', '')
        # code = address.get('country_code')
        # zipcode = address.get('postcode')
        # print(address)






