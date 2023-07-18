from django.shortcuts import render, redirect, HttpResponse
import requests
from .models import Coin
# Create your views here.

def coin_values(request):
    url = 'https://rest.coinapi.io/v1/exchangerate/BTC/USD'  # Example request for Bitcoin to USD
    headers = {'X-CoinAPI-Key' : '59B4DDDE-95FD-4054-B0EA-381081B01CDC'}
    
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        coin_value = data['rate']  # Extract the coin value from the response data

        # Pass the coin value to the template
        return render(request, 'success.html', {'coin_value': coin_value})
    else:
        return render(request, 'error.html')
    
def viewCoin(request):
    Coin.objects.all()
    return render(request,'view.html')