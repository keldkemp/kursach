from django.db import models
from django.urls import reverse, reverse_lazy


class Client(models.Model):
    name = models.CharField("Имя", max_length=150)
    address = models.CharField("Адрес", max_length=255, blank=True)
    phone_number = models.CharField("Телефон", max_length=50)
    email = models.CharField("Email", max_length=255, blank=True)

    def get_absolute_url(self):
        return reverse('client:client_detail', kwargs={'pk': self.pk})


class Realty(models.Model):
    name = models.CharField("Наименование", max_length=255)
    square = models.IntegerField("Площадь", blank=True, null=True)
    floor = models.IntegerField("Этаж", blank=True, null=True)
    rooms = models.IntegerField("Кол-во комнат", blank=True, null=True)
    address = models.CharField("Адрес", max_length=255)
    client_price = models.DecimalField("Стоимость", max_digits=9, decimal_places=2)
    description = models.TextField("Описание", max_length=10000, blank=True, null=True)

    def get_absolute_url(self):
        return reverse('realty:realty_detail', kwargs={'pk': self.pk})
