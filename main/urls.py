from django.urls import path
from main import views

urlpatterns = [
    path('', views.fetchCoinData, name='fetch-data'),
    path('/view/', views.viewCoin, name='view-coin')
]