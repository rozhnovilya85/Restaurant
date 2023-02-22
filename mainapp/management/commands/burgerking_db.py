
from django.core.management import BaseCommand
import json
import requests
from geopy.geocoders import Nominatim

from mainapp.models import RestaurantDB


class Command(BaseCommand):

    def handle(self, *args, **options):

        url = 'https://burgerkingrus.ru/order-app/api/v1/restaurants/search'
        response = requests.get(url)
        data = json.loads(response.text)
        all_rest = data['response']
        list_error = list()
        for item in all_rest:
            try:
                geolocator = Nominatim(user_agent="geoapiExercises")
                location = geolocator.reverse(item['latitude'] + "," + item['longitude'])
                address = location.raw['address']
                _city = address.get('city', '')

                rest_data = RestaurantDB(
                    name_rest=item['name'],
                    city=_city,
                    address=item['address'],
                    timezone=item['timezone'],
                    brand='burgerking',
                    is_active=item['is_active']
                )
                rest_data.save()
            except:
                rest_data = RestaurantDB(
                    name_rest=item['name'],
                    city='None',
                    address=item['address'],
                    timezone=item['timezone'],
                    brand='burgerking',
                    is_active=item['is_active']
                )
                rest_data.save()
                list_error.append(item)
        with open('log_burgerking.txt', 'w') as file:
            file.writelines(str(list_error))



