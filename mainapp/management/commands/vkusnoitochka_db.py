import time

from django.core.management import BaseCommand
import json
import requests
from geopy.geocoders import Nominatim

from mainapp.models import RestaurantDB


class Command(BaseCommand):

    def handle(self, *args, **options):

        url = 'https://vkusnoitochka.ru/api/restaurants'
        response = requests.get(url)
        data = json.loads(response.text)
        all_rest = data['restaurants']
        list_id = list()
        for item in all_rest:
            list_id.append(str(item['id']))

        list_rest = list()
        url_1 = 'https://vkusnoitochka.ru/api/restaurant/'
        for a in list_id:
            response = requests.get(url_1 + a)
            data_r = json.loads(response.text)
            rest = data_r['restaurant']
            list_rest.append(rest)
            time.sleep(0.2)
        list_error = list()
        for item in list_rest:
            try:
                rest_data = RestaurantDB(
                    name_rest=item['name'],
                    city=item['city'],
                    address=item['address'],
                    timezone=item['timezone'],
                    brand='vkusnoitochka',
                    is_active=item['isOpen']
                )
                rest_data.save()
            except:
                list_error.append(item)
        with open('log_vkusnoitochka.txt', 'w') as file:
            file.writelines(str(list_error))

