from agent.models import Service
from django.urls import reverse, reverse_lazy
from rules.contrib.views import PermissionRequiredMixin
from django_filters.views import FilterView
from django.views.generic import (
    CreateView, DeleteView, DetailView, FormView, UpdateView,
)
from agent.forms import (
    ServiceForm
)
from agent.filters import ServiceFilter


class List(PermissionRequiredMixin, FilterView):
    model = Service
    filterset_class = ServiceFilter
    template_name = 'agent/service/list.html'
    context_object_name = 'services'
    paginate_by = 25
    permission_required = 'service'


class Create(PermissionRequiredMixin, CreateView):
    model = Service
    form_class = ServiceForm
    template_name = 'agent/service/form.html'
    permission_required = 'service.add'


class Update(PermissionRequiredMixin, UpdateView):
    model = Service
    form_class = ServiceForm
    template_name = 'agent/service/form.html'
    permission_required = 'service.edit'


class Delete(PermissionRequiredMixin, DeleteView):
    model = Service
    template_name = 'agent/service/confirm_delete.html'
    success_url = reverse_lazy('service:service_list')
    permission_required = 'service.delete'


class Detail(PermissionRequiredMixin, DetailView):
    model = Service
    template_name = 'agent/service/detail.html'
    permission_required = 'service'
