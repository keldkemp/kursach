from django.db import models
from itertools import count
from django.contrib.auth import get_user_model
from transliterate import translit
from django.contrib.auth.models import AbstractUser, UserManager
from django.urls import reverse, reverse_lazy
from django.utils import timezone


class Client(models.Model):
    name = models.CharField("Имя", max_length=150)
    address = models.CharField("Адрес", max_length=255, blank=True)
    phone_number = models.CharField("Телефон", max_length=50)
    email = models.CharField("Email", max_length=255, blank=True)

    def get_absolute_url(self):
        return reverse('client:client_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name


class RealtyType(models.Model):
    name = models.CharField("Тип недвижимости", max_length=255, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('realty_type:realty_type_detail', kwargs={'pk': self.pk})


class Realty(models.Model):
    name = models.CharField("Наименование", max_length=255)
    realty_type = models.ForeignKey(
        RealtyType,
        on_delete=models.PROTECT,
        verbose_name="Тип недвижимости",
        null=True)
    square = models.IntegerField("Площадь", blank=True, null=True)
    land = models.IntegerField("Земля", blank=True, null=True)
    floor = models.IntegerField("Этаж", blank=True, null=True)
    rooms = models.IntegerField("Кол-во комнат", blank=True, null=True)
    address = models.CharField("Адрес", max_length=255)
    client_price = models.DecimalField("Стоимость", max_digits=15, decimal_places=2)
    description = models.TextField("Описание", max_length=10000, blank=True, null=True)

    def get_absolute_url(self):
        return reverse('realty:realty_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField("Услуга", max_length=255)
    price = models.DecimalField("Стоимость", max_digits=15, decimal_places=2)

    def get_absolute_url(self):
        return reverse('service:service_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name


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

    @property
    def is_manager(self) -> bool:
        return hasattr(self, 'agentmanager')


class Manager(models.Model):
    """
    Профиль риэлтора
    """
    user = models.OneToOneField(get_user_model(), on_delete=models.PROTECT)
    phone_number = models.CharField("Телефон", max_length=50, blank=True)

    def __str__(self):
        return self.user.get_full_name()


class AgentManager(models.Model):
    """
    Профиль Директора
    """
    user = models.OneToOneField(get_user_model(), on_delete=models.PROTECT)
    phone_number = models.CharField("Телефон", max_length=50, blank=True)

    def __str__(self):
        return self.user.get_full_name()


class Requests(models.Model):
    realty = models.OneToOneField(
        Realty,
        on_delete=models.PROTECT,
        verbose_name='Недвижимость'
    )
    worker = models.ForeignKey(
        Manager,
        on_delete=models.PROTECT,
        verbose_name='Сотрудник'
    )
    client_sell = models.ForeignKey(
        Client,
        on_delete=models.PROTECT,
        verbose_name='Клиент(создал заявку)',
        related_name='client_sell'
    )
    client_buy = models.ForeignKey(
        Client,
        on_delete=models.PROTECT,
        verbose_name='Клиент-покупатель',
        related_name='client_buy',
        null=True,
        blank=True
    )
    service = models.ForeignKey(
        Service,
        on_delete=models.PROTECT,
        verbose_name='Услуга'
    )
    date_from = models.DateTimeField('Дата открытия заявки', default=timezone.now)
    date_to = models.DateTimeField('Дата закртытия заявки', null=True, blank=True)
    closed = models.BooleanField('Заявка закрыта', default=0, blank=True)

    def get_absolute_url(self):
        return reverse('request:detail', kwargs={'pk': self.pk})

    def get_full_price(self):
        price = self.realty.client_price
        service_price = self.service.price
        full_price = (price * service_price) / 100 + price
        return full_price
