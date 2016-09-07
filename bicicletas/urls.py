from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.listar, name='listar'),
    url(r'^bicicleta/([0-9]*)/$', views.bicicleta_detail, name='details'),
    url(r'^bicicleta/new/$', views.bicicleta_new, name='new'),
    url(r'^bicicleta/([0-9]*)/edit/$', views.bicicleta_edit, name='edit'),
    url(r'^bicicleta/([0-9]*)/delete/$', views.bicicleta_delete, name='delete'),
]