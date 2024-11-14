import requests

currencies = {}
def get_currency_data():
    response  = requests.get("https://api.coinlore.net/api/tickers/")
    response = response.json()

    data = response['data']
    for  currnecy in data:
        currnecy_name = currnecy['name']
        
        currnecy_price = currnecy['price_usd']
        
        currencies[currnecy_name] = currnecy_price
        
    return currencies

print(get_currency_data())



def calculate(a, give_currency_name, get_currency_name):
    if give_currency_name in currencies and get_currency_name in currencies:
        
        result = (a*float(currencies[give_currency_name])) / float(currencies[get_currency_name])
        print(f"without {result}")
        
        result += 0.01 * result 
        
        return result
        
    else:
        
        print("not found")



print(f"result :    {calculate(100,"Bitcoin", "Ethereum")}")

