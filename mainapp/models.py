from django.db import models

# Create your models here.


class RestaurantDB(models.Model):
    brand = models.CharField(max_length=100, verbose_name='Бренд')
    name_rest = models.CharField(max_length=150, verbose_name='Название ресторана', unique=True, blank=True, null=True)
    city = models.CharField(max_length=150, verbose_name='Город')
    address = models.CharField(max_length=250, verbose_name='Адрес')
    timezone = models.CharField(max_length=100, verbose_name='Часовой пояс', blank=True, null=True)
    is_active = models.BooleanField(default=True, verbose_name='Открыт')



