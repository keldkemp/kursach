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
    realty_type = django_filters.ModelMultipleChoiceFilter(
        label='Тип недвижимости:',
        field_name='realty_type',
        queryset=models.RealtyType.objects.all(),
        widget=Select2MultipleWidget
    )

    name = django_filters.CharFilter(
        label='Поиск недвижимости',
        lookup_expr='icontains'
    )

    class Meta:
        model = models.Realty
        fields = ('id',)
        order_by_field = 'id'


class ServiceFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(
        label='Поиск услуги',
        lookup_expr='icontains'
    )

    class Meta:
        model = models.Realty
        fields = ('name',)


class RequestFilter(django_filters.FilterSet):
    closed = django_filters.BooleanFilter(field_name='closed')

    date_from = django_filters.DateFromToRangeFilter(field_name='date_from')
    date_to = django_filters.DateFromToRangeFilter(field_name='date_to')

    realty = django_filters.ModelMultipleChoiceFilter(
        label='Недвижимость:',
        field_name='realty__name',
        queryset=models.Realty.objects.all(),
        widget=Select2MultipleWidget
    )
    client_sell = django_filters.ModelMultipleChoiceFilter(
        label='Клиент-продавец:',
        field_name='client_sell__name',
        queryset=models.Client.objects.all(),
        widget=Select2MultipleWidget
    )
    client_buy = django_filters.ModelMultipleChoiceFilter(
        label='Клиент-покупатель:',
        field_name='client_buy__name',
        queryset=models.Client.objects.all(),
        widget=Select2MultipleWidget
    )
    worker = django_filters.ModelMultipleChoiceFilter(
        label='Сотрудник:',
        field_name='worker_id',
        queryset=models.Manager.objects.all(),
        widget=Select2MultipleWidget
    )

    class Meta:
        model = models.Requests
        fields = ('closed',)
