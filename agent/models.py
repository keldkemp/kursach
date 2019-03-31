from django.db import models
from itertools import count
from django.contrib.auth import get_user_model
from transliterate import translit
from django.contrib.auth.models import AbstractUser, UserManager
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
    client_price = models.DecimalField("Стоимость", max_digits=15, decimal_places=2)
    description = models.TextField("Описание", max_length=10000, blank=True, null=True)

    def get_absolute_url(self):
        return reverse('realty:realty_detail', kwargs={'pk': self.pk})


class CustomUserManager(UserManager):
    def generate_uniq_username(self, first_name, last_name, prefix='user'):
        for idx in count():
            trans_f = translit(first_name, language_code='ru', reversed=True)
            trans_l = translit(last_name, language_code='ru', reversed=True)
            name = f'{prefix}_{idx}_{trans_f}_{trans_l}'.lower()[:150]
            if not self.filter(username=name).exists():
                return name


class User(AbstractUser):
    objects = CustomUserManager()

    @property
    def is_agent(self) -> bool:
        return hasattr(self, 'manager')


class Manager(models.Model):
    """
    Профиль риэлтора
    """
    user = models.OneToOneField(get_user_model(), on_delete=models.PROTECT)
    phone_number = models.CharField("Телефон", max_length=50, blank=True)

    def __str__(self):
        return self.user.get_full_name()
