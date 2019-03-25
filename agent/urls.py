from django.urls import path, include

from agent.views import client

agent_urlpatterns = ([
    path('', client.List.as_view(), name='client_list'),
    path('new/', client.Create.as_view(), name='client_new'),
    path('<int:pk>/', client.Detail.as_view(), name='client_detail'),
    path('<int:pk>/update/', client.Update.as_view(), name='client_update'),
    path('<int:pk>/delete/', client.Delete.as_view(), name='client_delete'),

], 'client')

urlpatterns = [
    path('', include(agent_urlpatterns))
]
