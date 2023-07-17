from django.shortcuts import render, redirect
import requests
from .models import Coin
# Create your views here.

def fetchCoinData(request):
    url = 'https://api.coinapi.io/v1/assets'
    headers = {
        'X-CoinAPI-Key': '59B4DDDE-95FD-4054-B0EA-381081B01CDC'
    }

    response = requests.get(url,headers=headers)

    if response.status_code == 200:
        data = response.json()
        coins = []

        for coin_data in data:
            coin = Coin(
                name = coin_data['name'],
                price = coin_data['price'],
                market_cap =coin_data['market_cap_usd']
            )
            coins.append(coin)

        Coin.objects.bulk_create(coins)

        return redirect(request,'/view')
    else:
        return render(request,'error.html')
    
def viewCoin(request):
    coins = Coin.objects.all()
    return render(request,'views.html')