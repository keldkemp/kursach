from datetime import datetime, timedelta

import django_filters
from django import forms
from django.http import QueryDict
from phonenumber_field import modelfields

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
