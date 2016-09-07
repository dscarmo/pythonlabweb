from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.listar),
    url(r'^bicicleta/([0-9]*)/$', views.bicicleta_detail, name="details"),
]