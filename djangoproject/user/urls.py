from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    #path('', views.index, name='index'),
    #path('', TemplateView.as_view(template_name='index.htm'), name='index'),
    path('', views.index, name='index'),
    path('accounts/create', views.createAccount, name='createAccount'),
    path('accounts/signin', views.signin, name='signin'),
]