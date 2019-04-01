from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse, reverse_lazy
from django.views.generic import (
    RedirectView, TemplateView, UpdateView,
)
from agent.forms import ProfileManagerForm
from rules.contrib.views import PermissionRequiredMixin


class AgentLoginRedirectView(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        if self.request.user.is_anonymous:
            return reverse('accounts:agent_login')
        elif self.request.user.is_superuser:
            return reverse('admin:index')
        elif self.request.user.is_agent:
            return reverse('client:client_list')
        else:
            return reverse('accounts:agent_login')


class PasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    success_url = reverse_lazy('accounts:agent_profile')
    template_name = 'agent/auth/password-change.html'


class ProfileView(PermissionRequiredMixin, UpdateView):
    template_name = 'agent/auth/profile.html'
    success_url = reverse_lazy('accounts:agent_profile')
    permission_required = 'profile'

    def get_object(self, queryset=None):
        return self.request.user

    def get_form_class(self):
        if self.request.user.is_agent:
            return ProfileManagerForm
        else:
            return reverse('accounts:agent_login')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update(instance={
            'user': self.object,
            'detail':
                self.object.manager
        })
        return kwargs
