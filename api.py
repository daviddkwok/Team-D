import requests
api_key = 'M3TUAJLWM4IJG8U4'
url = f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey={api_key}"
response = requests.get(url)
data=response.json()
# 'Realtime Currency Exchange Rate'
print(data)