from django import forms
from django.contrib.auth import get_user_model
from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput
from betterforms.multiform import MultiModelForm

from .models import (
    Client, Realty, Manager, Service, RealtyType, Requests
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

        fields = ['name', 'realty_type', 'square',
                  'land', 'floor', 'rooms',
                  'address', 'client_price',
                  'description']
        widgets = {
            'address': forms.TextInput(attrs={"class": "form-control", "placeholder": "Адрес недвижимости"}),
            'name': forms.TextInput(attrs={"class": "form-control", "placeholder": "Однокомнатная квартира, дача, вилла"}),
            'square': forms.NumberInput(attrs={"class": "form-control", "placeholder": "15 кв.м"}),
            'land': forms.NumberInput(attrs={"class": "form-control", "placeholder": "15 соток"}),
            'floor': forms.NumberInput(attrs={"class": "form-control", "placeholder": "9 этажей"}),
            'rooms': forms.NumberInput(attrs={"class": "form-control", "placeholder": "3 комнаты"}),
            'client_price': forms.TextInput(attrs={"class": "form-control", "placeholder": "2 000 000 ₽"}),

        }


class RealtyTypeForm(Base):
    class Meta:
        model = RealtyType

        fields = ['name']

        widgets = {
            'name': forms.TextInput(attrs={"class": "form-control", "placeholder": "Дача, квартира, земельный участок"})
        }


class ServiceForm(Base):
    class Meta:
        model = Service
        fields = ['name', 'price']
        widgets = {
            'price': forms.TextInput(attrs={"class": "form-control", "placeholder": "10 %"}),

        }


class RequestForm(Base):
    class Meta:
        model = Requests
        fields = ['client_sell', 'realty',
                  'worker', 'service', 'date_from']


class RequestClosedForm(Base):
    class Meta:
        model = Requests
        fields = ['client_buy', 'date_to', 'closed']
        widgets = {
            'date_to': forms.TextInput(attrs={"placeholder": "27.03.2019 00:00"}),
        }


class ProfileUserForm(forms.ModelForm):
    fullname = forms.CharField(
        label='ФИО',
        widget=forms.TextInput(attrs={'data-name-edit': True})
    )

    class Meta:
        model = get_user_model()
        fields = ('username', 'first_name', 'last_name', 'email')
        widgets = {
            'first_name': forms.HiddenInput(),
            'last_name': forms.HiddenInput(),
            'email': forms.TextInput(attrs={"class": "form-control", "placeholder": "example@email.com"}),
        }
        labels = {
            'username': 'Логин'
        }

    def __init__(self, *args, **kwargs):
        initial = kwargs.pop('initial', {})
        instance = kwargs.get('instance', None)

        if instance:
            if initial is None:
                initial = {}
            initial['fullname'] = instance.get_full_name()

        super(ProfileUserForm, self).__init__(*args, initial=initial, **kwargs)


class ManagerForm(forms.ModelForm):
    class Meta:
        model = Manager
        fields = ('phone_number',)
        widgets = {
            'phone_number': forms.TextInput(attrs={"class": "form-control", "placeholder": "Номер телефона"}),
            }


class ProfileManagerForm(MultiModelForm):
    form_classes = {
        'user': ProfileUserForm,
        'detail': ManagerForm
    }
