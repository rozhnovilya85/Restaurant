
from django.core.management import BaseCommand
from mainapp.models import RestaurantDB
import pandas as pd



class Command(BaseCommand):

    def handle(self, *args, **options):
        burgerking_qs = RestaurantDB.objects.filter(brand='burgerking')
        kfc_qs = RestaurantDB.objects.filter(brand='kfc')
        vkusnoitochka_qs = RestaurantDB.objects.filter(brand='vkusnoitochka', is_active='True')
        q_b = burgerking_qs.values()
        q_k = kfc_qs.values()
        q_v = vkusnoitochka_qs.values()
        df_b = pd.DataFrame.from_records(q_b)
        df_k = pd.DataFrame.from_records(q_k)
        df_v = pd.DataFrame.from_records(q_v)

        df_b.to_excel('saved_ratings_1.xls')
        df_k.to_excel('saved_ratings_2.xls')
        df_v.to_excel('saved_ratings_3.xls')












