import requests

api_key = 'M3TUAJLWM4IJG8U4'
def api_function():
    # the API URL link for exchange rate from USD to SGD
    url = f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey={api_key}"

    # to request access to the data and assigned it to a object response
    response = requests.get(url)

    # retrieve data with .json from response and assigned it to a object data
    data = response.json()

    # gets the data of realtime currency exchange rate and assigned to an object exchange rate
    exchange_rate_dict = data['Realtime Currency Exchange Rate']

    # gets the exchange rate from the dictionary and stores the value in an object forex
    forex = exchange_rate_dict['5. Exchange Rate']

    # stores a message for real time currency conversion rate from usd to sgd using f-strings
    api_message = f'[REAL TIME CURRENCY CONVERSION RATE] USD1 = SGD{forex}'

    # shows the real time currency exchange rate from USD to SGD
    print(api_message)
