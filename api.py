import requests

api_key = 'M3TUAJLWM4IJG8U4'

# the API URL link for exchange rate from USD to SGD
url = f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey={api_key}"

# to request access to the data and assigned it to a object response
response = requests.get(url)

# retrieve data with .json from response and save it to a object data
data = response.json()
exchange_rate = data['Realtime Currency Exchange Rate']
forex = exchange_rate['5. Exchange Rate']
print(forex)