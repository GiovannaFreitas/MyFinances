from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('login', login, name='login'),
    path('create-account', create, name='criar-conta'),
    path('page-one', one, name='page-one'),
    path('poupanca', poupanca, name='poupança'),
]
