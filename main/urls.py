from django.urls import path
from main import views

urlpatterns = [
    path('', views.coin_values, name='coin-values')
]