from django.urls import path
from . import views


urlpatterns = [
    path('saiu_da_conta/', views.sair, name="sair"),
]