from django.urls import path
from . import views


urlpatterns = [
    path("licitacoes/", views.fetch_gazettes, name="fetch_gazettes"),
    path("exibir_gazettes", views.exibir_gazettes, name="exibir_gazettes"),
]
