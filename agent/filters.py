from datetime import datetime, timedelta

import django_filters
from django import forms
from django.http import QueryDict
from phonenumber_field import modelfields
from django_select2.forms import Select2MultipleWidget

from agent import models


class ClientFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(
        label='Искать по ФИО',
        lookup_expr='icontains'
    )

    class Meta:
        model = models.Client
        fields = ('name',)


class RealtyFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(
        label='Поиск недвижимости',
        lookup_expr='icontains'
    )

    class Meta:
        model = models.Realty
        fields = ('name',)


class ServiceFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(
        label='Поиск услуги',
        lookup_expr='icontains'
    )

    class Meta:
        model = models.Realty
        fields = ('name',)


class RequestFilter(django_filters.FilterSet):
    date = django_filters.BooleanFilter(field_name='closed')

    realty = django_filters.ModelMultipleChoiceFilter(
        label='Недвижимость:',
        field_name='realty__name',
        queryset=models.Realty.objects.all(),
        widget=Select2MultipleWidget
    )
    client = django_filters.ModelMultipleChoiceFilter(
        label='Клиент:',
        field_name='client_sell__name',
        queryset=models.Client.objects.all(),
        widget=Select2MultipleWidget
    )

    class Meta:
        model = models.Requests
        fields = ('closed',)
