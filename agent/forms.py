from django import forms
from django.contrib.auth import get_user_model
from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput
from betterforms.multiform import MultiModelForm

from .models import (
    Client, Realty, Manager
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
            'client_price': forms.TextInput(attrs={"class": "form-control", "placeholder": "2 000 000 ₽"}),

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
            'last_name': forms.HiddenInput()
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
