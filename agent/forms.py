from django import forms
from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput

from .models import (
    Client, Realty
)


class Base(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class ClientForm(Base):
    class Meta:
        model = Client

        fields = ['name', 'address',
                  'phone_number', 'email']
        widgets = {
            'address': forms.TextInput(attrs={"class": "form-control", "placeholder": "Адрес проживания"}),
            'name': forms.TextInput(attrs={"class": "form-control", "placeholder": "ФИО"}),
            'phone_number': forms.TextInput(attrs={"class": "form-control", "placeholder": "Номер телефона"}),
            'email': forms.EmailInput(attrs={"class": "form-control", "placeholder": "example@email.com"}),

        }


class RealtyForm(Base):
    class Meta:
        model = Realty

        fields = ['name', 'square',
                  'floor', 'rooms',
                  'address', 'client_price',
                  'description']
        widgets = {
            'address': forms.TextInput(attrs={"class": "form-control", "placeholder": "Адрес недвижимости"}),
            'name': forms.TextInput(attrs={"class": "form-control", "placeholder": "Однокомнатная квартира, дача, вилла"}),
            'square': forms.NumberInput(attrs={"class": "form-control", "placeholder": "15"}),
            'floor': forms.NumberInput(attrs={"class": "form-control", "placeholder": "9"}),
            'rooms': forms.NumberInput(attrs={"class": "form-control", "placeholder": "3"}),
            'client_price': forms.NumberInput(attrs={"class": "form-control", "placeholder": "2 000 000 ₽"}),

        }
