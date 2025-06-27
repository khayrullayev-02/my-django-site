from django.urls import path
from .views import loyha_list

urlpatterns = [
    path('', loyha_list, name='loyha_list'),
]
