
from django.core.management import BaseCommand
import json
import requests


from mainapp.models import RestaurantDB


class Command(BaseCommand):

    def handle(self, *args, **options):
        burgerking_count = RestaurantDB.objects.filter(brand='burgerking').count()
        kfc_count = RestaurantDB.objects.filter(brand='kfc').count()
        vkusnoitochka_count = RestaurantDB.objects.filter(brand='vkusnoitochka', is_active='True').count()
        print(f'Количество ресторанов Бургеркинг в России состовляет: {burgerking_count}')
        print(f'Количество ресторанов KFC в России состовляет: {kfc_count}')
        print(f'Количество ресторанов Вкусно и Точка в России состовляет: {vkusnoitochka_count}')






