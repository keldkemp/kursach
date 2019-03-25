from django import forms
from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput

from .models import (
    Client
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
