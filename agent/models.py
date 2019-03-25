from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.urls import reverse, reverse_lazy


class Client(models.Model):
    name = models.CharField("Имя", max_length=150)
    address = models.CharField("Адрес", max_length=255, blank=True)
    phone_number = models.CharField("Телефон", max_length=50)
    email = models.CharField("Email", max_length=255, blank=True)

    def get_absolute_url(self):
        return reverse('client:client_detail', kwargs={'pk': self.pk})
