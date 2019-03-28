from django.urls import path, include

from agent.views import client, realty

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

urlpatterns = [
    path('realty/', include(realty_urlpatterns)),
    path('client/', include(agent_urlpatterns)),
    path('', client.redirect),
]
