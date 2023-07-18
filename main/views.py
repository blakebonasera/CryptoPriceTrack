from django.shortcuts import render, redirect, HttpResponse
import requests
from .models import Coin
# Create your views here.

def coin_values(request):
    if request.method == 'POST':
        coin_symbol = request.POST.get('coin_symbol')

        # Make a GET request to the CoinAPI API
        url = f'https://rest.coinapi.io/v1/exchangerate/{coin_symbol}/USD'  # Example request for selected coin to USD
        headers = {
            'X-CoinAPI-Key': '59B4DDDE-95FD-4054-B0EA-381081B01CDC',  # Replace with your CoinAPI API key
        }

        response = requests.get(url, headers=headers)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            data = response.json()
            coin_value = data['rate']  # Extract the coin value from the response data

            # Pass the coin value to the template
            return render(request, 'coin_values.html', {'coin_value': coin_value, 'coin_symbol': coin_symbol})
        else:
            return render(request, 'error.html')

    return render(request, 'search.html')
    
