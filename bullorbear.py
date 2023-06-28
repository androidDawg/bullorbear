# For PSE. 
# some references: https://pypi.org/project/mistermarket/#description
# mainly using API: http://phisix-api4.appspot.com/index.html


import requests
import talib as ta

def get_latest_data(symbol):
    url = f"http://phisix-api.appspot.com/stocks/{symbol}.json"
    response = requests.get(url)
    data = response.json()
    return data

symbol = "AREIT"
data = get_stock_data(symbol)
amount = data['stock'][0]['price']['amount']
volume = data['stock'][0]['volume']

print(f"Amount: {amount}")
print(f"Volume: {volume}")
