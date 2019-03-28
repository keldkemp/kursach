from agent.models import Realty
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django_filters.views import FilterView
from django.views.generic import (
    CreateView, DeleteView, DetailView, FormView, UpdateView,
)
from agent.forms import (
    RealtyForm
)
from agent.filters import RealtyFilter


class List(FilterView):
    model = Realty
    filterset_class = RealtyFilter
    template_name = 'agent/realty/list.html'
    context_object_name = 'realtys'
    paginate_by = 25


class Create(CreateView):
    model = Realty
    form_class = RealtyForm
    template_name = 'agent/realty/form.html'


class Update(UpdateView):
    model = Realty
    form_class = RealtyForm
    template_name = 'agent/realty/form.html'


class Delete(DeleteView):
    model = Realty
    template_name = 'agent/realty/confirm_delete.html'
    success_url = reverse_lazy('realty:realty_list')


class Detail(DetailView):
    model = Realty
    template_name = 'agent/realty/detail.html'
