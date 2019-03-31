from django.contrib import admin
from agent import models
from django.contrib.auth.forms import (
    UserChangeForm, UserCreationForm, UsernameField,
)
from django.contrib.auth.admin import UserAdmin


@admin.register(models.Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone_number', 'email')


@admin.register(models.Manager)
class ManagerAdmin(admin.ModelAdmin):
    list_display = ('get_manager_full_name', 'user')

    def get_manager_full_name(self, obj: models.Manager):
        return obj.user.get_full_name()


class TenantUserCreateForm(UserCreationForm):
    class Meta:
        models = models.User
        fields = ('username',)
        field_classes = {'username': UsernameField}


class TenantUserChangeForm(UserChangeForm):
    class Meta:
        models = models.User
        fields = '__all__'
        field_classes = {'username': UsernameField}


@admin.register(models.User)
class TenantUserAdmin(UserAdmin):
    form = TenantUserChangeForm
    add_form = TenantUserCreateForm
