from django.urls import path
from main import views

urlpatterns = [
    path('', views.fetchCoinData),
    path('view/', views.viewCoin)
]