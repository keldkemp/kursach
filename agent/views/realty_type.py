from agent.models import RealtyType
from rules.contrib.views import PermissionRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django_filters.views import FilterView
from django.views.generic import (
    CreateView, DeleteView, DetailView, FormView, UpdateView,
)
from agent.forms import (
    RealtyTypeForm
)
from agent.filters import RealtyFilter


class List(PermissionRequiredMixin, FilterView):
    model = RealtyType
    filterset_class = RealtyFilter
    template_name = 'agent/realtytype/list.html'
    context_object_name = 'realtys'
    paginate_by = 25
    permission_required = 'realty_type'


class Create(PermissionRequiredMixin, CreateView):
    model = RealtyType
    form_class = RealtyTypeForm
    template_name = 'agent/realtytype/form.html'
    permission_required = 'realty_type.add'


class Update(PermissionRequiredMixin, UpdateView):
    model = RealtyType
    form_class = RealtyTypeForm
    template_name = 'agent/realtytype/form.html'
    permission_required = 'realty_type.edit'


class Delete(PermissionRequiredMixin, DeleteView):
    model = RealtyType
    template_name = 'agent/realtytype/confirm_delete.html'
    success_url = reverse_lazy('realty_type:realty_type_list')
    permission_required = 'realty_type.delete'


class Detail(PermissionRequiredMixin, DetailView):
    model = RealtyType
    template_name = 'agent/realtytype/detail.html'
    permission_required = 'realty_type'
