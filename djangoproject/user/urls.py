from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('account', views.account, name='account'),
    path('accounts/create', views.createAccount, name='createAccount'),
    path('accounts/signin', views.signin, name='signin'),
    path('accounts/signout', views.signout, name='signout'),
    path('player/create', views.createPlayer, name='createPlayer'),
    path('player/accountsPlayers', views.getAccountsPlayers, name='getPlayersFromAccount'),
    
]