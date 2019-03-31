from agent.models import Client
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from rules.contrib.views import PermissionRequiredMixin
from django_filters.views import FilterView
from django.views.generic import (
    CreateView, DeleteView, DetailView, FormView, UpdateView,
)
from agent.forms import (
    ClientForm
)
from agent.filters import ClientFilter


class List(PermissionRequiredMixin, FilterView):
    model = Client
    filterset_class = ClientFilter
    template_name = 'agent/client/list.html'
    context_object_name = 'clients'
    paginate_by = 25
    permission_required = 'client'


class Create(PermissionRequiredMixin, CreateView):
    model = Client
    form_class = ClientForm
    template_name = 'agent/client/form.html'
    permission_required = 'client.add'


class Update(PermissionRequiredMixin, UpdateView):
    model = Client
    form_class = ClientForm
    template_name = 'agent/client/form.html'
    permission_required = 'client.edit'


class Delete(PermissionRequiredMixin, DeleteView):
    model = Client
    template_name = 'agent/client/confirm_delete.html'
    success_url = reverse_lazy('client:client_list')
    permission_required = 'client.delete'


class Detail(PermissionRequiredMixin, DetailView):
    model = Client
    template_name = 'agent/client/detail.html'
    permission_required = 'client'
