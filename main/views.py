from django.shortcuts import render, redirect, HttpResponse
import requests
from .models import Coin
# Create your views here.

def fetchCoinData(request):
    url = 'https://rest.coinapi.io/v1/symbols'
    headers = {'X-CoinAPI-Key' : '59B4DDDE-95FD-4054-B0EA-381081B01CDC'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        coins = []

        for coin_data in data:
            coin = Coin(
                name = coin_data['symbol_id'],
                price = coin_data['price'],
                volume = coin_data['volume_1day_usd']
            )
            coins.append(coin)

        Coin.objects.bulk_create(coins)

        return render(request,'success.html')
    else:
        return render(request,'error.html')
    
def viewCoin(request):
    coins = Coin.objects.all()
    return render(request,'views.html')