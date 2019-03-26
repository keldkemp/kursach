from django.contrib import admin
from agent import models


@admin.register(models.Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone_number', 'email')
