from django.urls import path, include
from django.contrib.auth import views as auth_views

from agent.views import client, realty, auth, service, realty_type, request

auth_urlpatterns = ([
    path('', auth.AgentLoginRedirectView.as_view()),
    path(
        'login/',
        auth_views.LoginView.as_view(template_name='agent/auth/login.html'),
        name='agent_login'
    ),
    path('logout/', auth_views.LogoutView.as_view(), name='agent_logout'),
    path(
        'redirect/',
        auth.AgentLoginRedirectView.as_view(),
        name='login-redirect'
    ),
    path(
        'password-change/',
        auth.PasswordChangeView.as_view(),
        name='agent_password-change'
    ),
    path('profile/', auth.ProfileView.as_view(), name='agent_profile'),

], 'accounts')


agent_urlpatterns = ([
    path('', client.List.as_view(), name='client_list'),
    path('new/', client.Create.as_view(), name='client_new'),
    path('<int:pk>/', client.Detail.as_view(), name='client_detail'),
    path('<int:pk>/update/', client.Update.as_view(), name='client_update'),
    path('<int:pk>/delete/', client.Delete.as_view(), name='client_delete'),

], 'client')

realty_urlpatterns = ([
    path('', realty.List.as_view(), name='realty_list'),
    path('new/', realty.Create.as_view(), name='realty_new'),
    path('<int:pk>/', realty.Detail.as_view(), name='realty_detail'),
    path('<int:pk>/update/', realty.Update.as_view(), name='realty_update'),
    path('<int:pk>/delete/', realty.Delete.as_view(), name='realty_delete'),
], 'realty')

realty_type_urlpatterns = ([
    path('', realty_type.List.as_view(), name='realty_type_list'),
    path('new/', realty_type.Create.as_view(), name='realty_type_new'),
    path('<int:pk>/', realty_type.Detail.as_view(), name='realty_type_detail'),
    path('<int:pk>/update/', realty_type.Update.as_view(), name='realty_type_update'),
    path('<int:pk>/delete/', realty_type.Delete.as_view(), name='realty_type_delete'),
], 'realty_type')

service_urlpatterns = ([
    path('', service.List.as_view(), name='service_list'),
    path('new/', service.Create.as_view(), name='service_new'),
    path('<int:pk>/', service.Detail.as_view(), name='service_detail'),
    path('<int:pk>/update/', service.Update.as_view(), name='service_update'),
    path('<int:pk>/delete/', service.Delete.as_view(), name='service_delete'),
], 'service')

request_urlpatterns = ([
    path('', request.List.as_view(), name='list'),
    path('archive', request.Archive.as_view(), name='archive'),
    path('new/', request.Create.as_view(), name='new'),
    path('<int:pk>/', request.Detail.as_view(), name='detail'),
    path('<int:pk>/update/', request.Update.as_view(), name='update'),
    path('<int:pk>/delete/', request.Delete.as_view(), name='delete'),
    path('<int:pk>/closed/', request.Closed.as_view(), name='closed'),
], 'request')

urlpatterns = [
    path('accounts/', include(auth_urlpatterns)),
    path('realty/', include(realty_urlpatterns)),
    path('realty-type/', include(realty_type_urlpatterns)),
    path('client/', include(agent_urlpatterns)),
    path('service/', include(service_urlpatterns)),
    path('request/', include(request_urlpatterns)),
    path('', auth.AgentLoginRedirectView.as_view()),
]
