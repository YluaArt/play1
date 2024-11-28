import requests


def get_course():
    url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=1"
    currencies = {}
    response = requests.get(url)
    for currency in response.json():
        id = currency["id"]
        name=currency ["name"]
        symbol = currency["symbol"]
        url_image = currency['image']
        course = currency["current_price"]
        currency = ["current_price"]
        currency = {
    
            "name":name,
            "symbol":symbol,
            "url_image":url_image,
            "course":course
        }
        currencies[id] = currency
    
    print(currencies)
    return currencies
    
