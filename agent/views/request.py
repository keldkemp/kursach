from agent.models import Requests
from django.urls import reverse, reverse_lazy
from rules.contrib.views import PermissionRequiredMixin
from django_filters.views import FilterView
from django.views.generic import (
    CreateView, DeleteView, DetailView, FormView, UpdateView,
)
from agent.forms import (
    RequestForm, RequestClosedForm
)
from agent.filters import RequestFilter


class List(PermissionRequiredMixin, FilterView):
    model = Requests
    filterset_class = RequestFilter
    template_name = 'agent/request/list.html'
    context_object_name = 'requests'
    paginate_by = 25
    permission_required = 'request'


class Archive(PermissionRequiredMixin, FilterView):
    model = Requests
    filterset_class = RequestFilter
    template_name = 'agent/request/archive.html'
    context_object_name = 'requests'
    paginate_by = 25
    permission_required = 'request'


class Create(PermissionRequiredMixin, CreateView):
    model = Requests
    form_class = RequestForm
    template_name = 'agent/request/form.html'
    permission_required = 'request.add'


class Update(PermissionRequiredMixin, UpdateView):
    model = Requests
    form_class = RequestForm
    template_name = 'agent/request/form.html'
    permission_required = 'request.edit'


class Delete(PermissionRequiredMixin, DeleteView):
    model = Requests
    template_name = 'agent/request/confirm_delete.html'
    success_url = reverse_lazy('request:list')
    permission_required = 'request.delete'


class Detail(PermissionRequiredMixin, DetailView):
    model = Requests
    template_name = 'agent/request/detail.html'
    permission_required = 'request'


class Closed(PermissionRequiredMixin, UpdateView):
    model = Requests
    form_class = RequestClosedForm
    template_name = 'agent/request/closed.html'
    permission_required = 'request.closed'
